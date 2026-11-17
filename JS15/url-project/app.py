import json
import pickle

import numpy as np
import tensorflow as tf
from flask import Flask, request, render_template_string

from pbl_url import lexical_features, normalize_url

app = Flask(__name__)

# Load Model, Scaler & Label
MODEL_PATH = 'url_model.h5'
SCALER_PATH = 'scaler.pkl'
LABELS_PATH = 'labels.json'
BENIGN = {'benign', 'legitimate'}

try:
    model = tf.keras.models.load_model(MODEL_PATH, compile=False)
    with open(SCALER_PATH, 'rb') as f:
        scaler = pickle.load(f)
    with open(LABELS_PATH) as f:
        labels = json.load(f)
    print("✅ System Loaded Successfully")
except Exception as e:
    print(f"❌ Error loading system: {e}")

def preprocess_url(url):
    # Preprocessing harus sama persis dengan training: normalisasi -> 28 fitur leksikal -> log1p -> scaler
    feats = lexical_features([normalize_url(url)]).clip(lower=0)
    return scaler.transform(np.log1p(feats.to_numpy(np.float32)))

FORM = '''
<div style="max-width:640px; margin:auto; padding:40px; font-family:sans-serif; text-align:center;">
    <h1>Malicious URL Detector</h1>
    <form action="/predict" method="post">
        <input type="text" name="url" placeholder="contoh: paypal-verify.example.xyz/login" required maxlength="2048"
               style="width:100%; padding:10px; font-size:16px;"><br><br>
        <button type="submit">Prediksi</button>
    </form>
</div>
'''

RESULT = '''
<div style="max-width:640px; margin:auto; padding:40px; font-family:sans-serif; text-align:center;">
    <h2>Hasil: <b>{{ label }}</b> ({{ verdict }})</h2>
    <p style="word-break:break-all;">{{ url }}</p>
    <table style="margin:auto;">{% for name, p in probs %}<tr><td>{{ name }}</td><td>{{ '%.3f'|format(p) }}</td></tr>{% endfor %}</table>
    <p><a href="/">Kembali</a></p>
</div>
'''

@app.route('/', methods=['GET'])
def home():
    return render_template_string(FORM)

@app.route('/predict', methods=['POST'])
def predict():
    url = request.form.get('url', '').strip()
    if not url or len(url) > 2048:
        return render_template_string("<h2 style='text-align:center'>Input tidak valid: isi URL (maksimal 2048 karakter).</h2><center><a href='/'>Kembali</a></center>"), 400
    try:
        proba = model.predict(preprocess_url(url), verbose=0)[0]
    except Exception as e:
        return f"Error: {e}", 500
    label = labels[int(proba.argmax())]
    verdict = 'aman' if label in BENIGN else 'berbahaya'
    probs = sorted(zip(labels, proba.tolist()), key=lambda t: -t[1])
    return render_template_string(RESULT, label=label, verdict=verdict, url=url, probs=probs)

if __name__ == '__main__':
    # Port 7860 wajib untuk Hugging Face Spaces
    app.run(host='0.0.0.0', port=7860)
