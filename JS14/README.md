# JS14 - Convolutional Neural Network

[Modul sumber](https://polinema.gitbook.io/jti-modul-praktikum-pembelajaran-mesin-2025-2026/js14-convolutional-neural-network). Gunakan kernel `.venv` dan jalankan notebook dari folder ini.

- [Praktikum 1 - Klasifikasi cat vs dog](Praktikum_1_244107020049_Agus.ipynb)
- [Praktikum 2 - Klasifikasi CIFAR-10](Praktikum_2_244107020049_Agus.ipynb)
- [Tugas Praktikum - CNN CIFAR-10 > 80% dan CNN MNIST](Tugas_Praktikum_244107020049_Agus.ipynb)
- [Eksperimen tambahan - CNN untuk data teks (IMDB dan 20 Newsgroups)](Eksperimen_CNN_Teks_244107020049_Agus.ipynb)

Dataset: [provenance](data/provenance.json). Arsip cat-dog (233 MB) tidak di-commit karena melebihi batas GitHub. Notebook Praktikum 1 mengunduhnya dari Google Drive modul dan memverifikasi SHA-256 secara otomatis.

## Penyesuaian dari modul

- `ImageDataGenerator` sudah dihapus di Keras 3. Penggantinya `image_dataset_from_directory` dengan layer `Rescaling`, `RandomShear`, `RandomZoom`, dan `RandomFlip` yang memakai parameter sama.
- Prediksi satu citra memakai threshold `> 0.5`, bukan `== 1`, dan citra dibagi 255 seperti data latih.
- Tugas CIFAR-10 memilih epoch dari data validasi (5.000 citra latih), bukan dari data test.

## CNN untuk teks

Sesuai arahan dosen, notebook eksperimen mengulang langkah Praktikum 1 dan 2 pada data teks. `Conv2D` diganti `Embedding` + `Conv1D`. Hasilnya dibandingkan dengan Kim-CNN dan baseline TF-IDF + model linier, disertai rujukan jurnal.
