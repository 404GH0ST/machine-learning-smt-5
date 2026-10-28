# JS11 - Klasifikasi SVM

[Modul sumber](https://polinema.gitbook.io/jti-modul-praktikum-pembelajaran-mesin-2025-2026/js11-klasifikasi-2). Gunakan kernel **Python (Miniconda ml-praktikum)** dan jalankan notebook dari folder ini.

- [Praktikum 1 - SVM Data Dummy Linier](Praktikum_1_244107020049_Agus.ipynb)
- [Praktikum 2 - SVM Data Dummy Non-Linier](Praktikum_2_244107020049_Agus.ipynb)
- [Praktikum 3 - SVM Data Overlapping](Praktikum_3_244107020049_Agus.ipynb)
- [Praktikum 4 - Klasifikasi Citra Wajah](Praktikum_4_244107020049_Agus.ipynb)
- [Praktikum 5 - Klasifikasi Citra Siang dan Malam](Praktikum_5_244107020049_Agus.ipynb)
- [Tugas Praktikum - SVM Suara dan Histogram Siang/Malam](Tugas_Praktikum_244107020049_Agus.ipynb)

Dataset: [provenance dan checksum](data/provenance.json).

Kode praktikum mengikuti modul; penyesuaian dijelaskan pada notebook masing-masing. Cara menjalankan tersedia di [README utama](../README.md).

## Kesesuaian instruksi GitBook

Praktikum 1 mempertahankan ilustrasi dummy, margin, support vectors, dan widget jumlah sampel. Sesuai pengantar modul, ditambahkan dataset pilihan sendiri Breast Cancer Wisconsin (Diagnostic) dari UCI melalui scikit-learn, beserta split, standardisasi, klasifikasi SVM linier, evaluasi, dan analisis. Praktikum 2–3 mencakup proyeksi radial/3D, kernel RBF, serta pengaruh C pada data overlapping. Praktikum 4 mencakup LFW, PCA, GridSearchCV, prediksi, classification report, dan confusion matrix. Praktikum 5 mencakup visualisasi sebelum/sesudah preprocessing, fitur kecerahan, threshold 120, serta SVM dan evaluasi train/test.

Tugas suara memuat enam kombinasi (split 70:30 dan 80:20, masing-masing kernel linear/poly/RBF), dengan tabel akurasi. Tugas citra memakai dataset Praktikum 5, histogram HSV, split 80:20, SVM RBF, tuning, dan akurasi. Path lokal dan koreksi kompatibilitas tidak mengubah tujuan langkah modul.
