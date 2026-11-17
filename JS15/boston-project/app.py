import numpy as np
import pickle
import tensorflow as tf
from flask import Flask, request, render_template_string

app = Flask(__name__)

# Load Model & Scaler
MODEL_PATH = 'boston_model.h5'
SCALER_PATH = 'scaler.pkl'

# Urutan fitur HARUS sama dengan kolom saat training (dataset Boston Housing)
FEATURES = [
    ('CRIM', 'Tingkat kriminalitas per kapita', 0.1),
    ('ZN', 'Proporsi lahan hunian kavling > 25.000 sq.ft (%)', 0.0),
    ('INDUS', 'Proporsi lahan bisnis non-ritel (%)', 7.0),
    ('CHAS', 'Berbatasan dengan Sungai Charles (1 = ya, 0 = tidak)', 0),
    ('NOX', 'Konsentrasi nitrogen oksida (ppm / 10 juta)', 0.5),
    ('RM', 'Rata-rata jumlah kamar per rumah', 6.2),
    ('AGE', 'Proporsi rumah dibangun sebelum 1940 (%)', 65.0),
    ('DIS', 'Jarak berbobot ke 5 pusat kerja Boston', 4.0),
    ('RAD', 'Indeks akses ke jalan raya radial', 4),
    ('TAX', 'Pajak properti per USD 10.000', 300),
    ('PTRATIO', 'Rasio murid-guru', 18.0),
    ('B', 'Variabel B dataset asli', 390.0),
    ('LSTAT', 'Persentase penduduk berstatus rendah (%)', 12.0),
]

try:
    # compile=False: hanya inferensi; metrik 'mse' format .h5 lama tidak perlu dideserialisasi di Keras 3
    model = tf.keras.models.load_model(MODEL_PATH, compile=False)
    with open(SCALER_PATH, 'rb') as f:
        scaler = pickle.load(f)
    print("✅ System Loaded Successfully")
except Exception as e:
    print(f"❌ Error loading system: {e}")

def preprocess_features(form):
    # Ambil 13 fitur sesuai urutan training, lalu normalisasi dengan scaler training
    values = []
    for name, _, _ in FEATURES:
        raw = form.get(name, '').strip().replace(',', '.')
        try:
            value = float(raw)
        except ValueError:
            raise ValueError(f"Nilai {name} harus berupa angka.")
        if not np.isfinite(value):
            raise ValueError(f"Nilai {name} tidak valid.")
        values.append(value)
    return scaler.transform(np.array(values).reshape(1, -1))

FORM = '''
<div style="max-width:640px; margin:auto; padding:30px; font-family:sans-serif;">
    <h1 style="text-align:center">Prediksi Harga Rumah Boston</h1>
    <form action="/predict" method="post">
        {% for name, label, default in features %}
        <label style="display:flex; justify-content:space-between; gap:12px; margin:6px 0;">
            <span>{{ label }} ({{ name }})</span>
            <input name="{{ name }}" value="{{ default }}" inputmode="decimal" required style="width:110px">
        </label>
        {% endfor %}
        <p style="text-align:center"><button type="submit">Prediksi</button></p>
    </form>
</div>
'''

@app.route('/', methods=['GET'])
def home():
    return render_template_string(FORM, features=FEATURES)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = preprocess_features(request.form)
    except ValueError as e:
        return render_template_string("<h2 style='text-align:center'>Input tidak valid: {{ msg }}</h2><center><a href='/'>Kembali</a></center>", msg=str(e)), 400
    try:
        prediction = float(model.predict(data, verbose=0)[0][0])
        return f"<h2 style='text-align:center'>Perkiraan harga median: USD {prediction:.2f} ribu</h2><center><a href='/'>Kembali</a></center>"
    except Exception as e:
        return f"Error: {e}", 500

if __name__ == '__main__':
    # Port 7860 wajib untuk Hugging Face Spaces
    app.run(host='0.0.0.0', port=7860)
