# JS13 - Artificial Neural Network (ANN) dan Evaluasi Classifier

[Modul sumber](https://polinema.gitbook.io/jti-modul-praktikum-pembelajaran-mesin-2025-2026/js13-artificial-neural-network-ann-dan-evaluasi-classifier). Gunakan kernel `.venv` (Python 3.12) dan jalankan notebook dari folder ini.

- [Praktikum 1 - JST 2 layer manual (XOR) + Tugas 1](Praktikum_1_244107020049_Agus.ipynb)
- [Praktikum 2 - Klasifikasi Iris dengan Keras + Tugas 2 dan 3](Praktikum_2_244107020049_Agus.ipynb)
- [Praktikum 3 - Regresi data dummy + Tugas 4, MLP Boston Housing](Praktikum_3_244107020049_Agus.ipynb)
- [Tugas Praktikum - JST MNIST dan eksperimen parameter](Tugas_Praktikum_244107020049_Agus.ipynb)

Dataset: [provenance](data/provenance.json). Kode utama mengikuti modul dan memakai dataset modul. Penyesuaian kompatibilitasnya:

- `OneHotEncoder(sparse=False)` → `sparse_output=False`.
- `input_shape` dipindah ke layer `Input` (Keras 3).
- `load_boston` sudah dihapus sejak scikit-learn 1.2, sehingga data Boston yang sama dibaca dari sumber asli StatLib (`data/boston.txt`).

Setiap perbandingan konfigurasi dijalankan pada beberapa seed. Analisisnya merujuk jurnal yang dicantumkan di bagian *Rujukan* tiap notebook.
