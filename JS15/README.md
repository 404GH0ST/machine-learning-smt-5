# JS15 - Pipeline Machine Learning & Deployment

[Modul sumber](https://polinema.gitbook.io/jti-modul-praktikum-pembelajaran-mesin-2025-2026/js15-pipeline-machine-learning-and-deployment). Gunakan kernel `.venv` dan jalankan notebook dari folder ini.

- [Praktikum 1 - Day vs Night: HOG + Neural Network, ekspor `.h5` dan `.pkl`](Praktikum_1_244107020049_Agus.ipynb)
- [Praktikum 2 - Flask + Docker untuk Hugging Face, uji endpoint lokal](Praktikum_2_244107020049_Agus.ipynb), berkas deploy di [daynight-project/](daynight-project/)
- [Tugas - pipeline deployment model sendiri (MLP harga rumah Boston dari JS13)](Tugas_Praktikum_244107020049_Agus.ipynb), berkas deploy di [boston-project/](boston-project/)

Dataset: lampiran modul `images.zip` ([provenance](data/provenance.json)).

## Status deployment

Kedua aplikasi sudah diuji secara lokal, baik dengan Flask test client di notebook maupun dengan server `python app.py` di port 7860 yang diakses lewat `curl`. Push ke Hugging Face Spaces memerlukan akun dan access token pribadi, sehingga dilakukan sendiri:

```sh
git lfs install
git clone https://huggingface.co/spaces/USERNAME_ANDA/NAMA_SPACE      # Space baru, SDK Docker
cp JS15/daynight-project/* NAMA_SPACE/                                 # atau JS15/boston-project/*
cd NAMA_SPACE && git add . && git commit -m "Deploy aplikasi ke HF" && git push
```

Perbedaan dari modul:

- Base image `python:3.12-slim` karena `tensorflow-cpu` 2.21 membutuhkan Python ≥ 3.10.
- Versi di `requirements.txt` dikunci sama dengan environment training.
- Model disimpan dengan `include_optimizer=False` (18 MB, bukan 53 MB).
- `README.md` berisi header konfigurasi Space.

## PBL - Malicious URL Detection

[PBL_Malicious_URL_244107020049_Agus.ipynb](PBL_Malicious_URL_244107020049_Agus.ipynb) menerapkan langkah jobsheet ini pada dataset PBL `Malicious URL Detection.csv` (783.705 URL, 7 kelas). Fitur bersama ada di [`pbl_url.py`](../pbl_url.py).

Deploy PBL ada di [url-project/](url-project/): detektor URL berbahaya (Flask + Docker) memakai model `url_model.h5`, `scaler.pkl`, dan `pbl_url.py` yang sama dengan training.
