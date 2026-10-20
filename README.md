# Praktikum Pembelajaran Mesin

Nama: **Agus** · NIM: **244107020049**

Pengerjaan lima modul [GitBook Polinema 2025/2026](https://polinema.gitbook.io/jti-modul-praktikum-pembelajaran-mesin-2025-2026). Notebook menggunakan kernel **Python (Miniconda ml-praktikum)**. Kode utama praktikum mengikuti urutan dan blok kode modul; penyesuaian kompatibilitas dijelaskan pada notebook masing-masing. Evaluasi tambahan diletakkan setelah langkah modul.

| Modul | Folder | Praktikum | Tugas |
| --- | --- | --- | --- |
| JS05 Klasterisasi Hierarki | [JS05](JS05/) | 1–2: HDBSCAN, eksperimen parameter, evaluasi | HDBSCAN pada Iris |
| JS06 Approximate Nearest Neighbors | [JS06](JS06/) | 1–6: Annoy, FAISS, HNSW, recall/QPS, Spotify | Perbandingan Colab/PyDroid3, spesifikasi HP, dan analisis hasil |
| JS06 Regresi | [JS06_Regresi](JS06_Regresi/) | 1: OLS; 2: SVR | Multiple Linear Regression biaya medis |
| JS09 Klasifikasi | [JS09](JS09/) | 1: kNN; 2–3: Naive Bayes | 1: fitur/k suara; 2: CountVectorizer vs TF-IDF |
| JS11 Klasifikasi 2 | [JS11](JS11/) | 1–3: SVM sintetis; 4: wajah; 5: siang/malam | SVM suara dan histogram HSV siang/malam |

Total **24 notebook: 18 praktikum dan 6 tugas**. Seluruh **24 notebook menyimpan output dan telah divalidasi di Jupyter Miniconda**. Notebook tugas ANN mengolah hasil Colab/PyDroid3 yang dikirim pengguna; angka pengukuran perangkat tidak diganti dengan benchmark lokal. Dua modul bernomor JS06 dipisahkan agar ANN dan regresi tidak saling menimpa. File menggunakan pola `Praktikum_N_244107020049_Agus.ipynb` dan `Tugas_Praktikum_244107020049_Agus.ipynb`; JS09 memiliki `Tugas_1` dan `Tugas_2`.

## Menjalankan di Jupyter Miniconda

Environment yang digunakan pada komputer ini berada di `/Volumes/External/miniconda3/envs/ml-praktikum`.

```sh
conda activate ml-praktikum
python -m ipykernel install --user --name ml-praktikum --display-name "Python (Miniconda ml-praktikum)"
jupyter lab
```

Buka notebook dari folder modulnya, pilih kernel **Python (Miniconda ml-praktikum)**, lalu **Restart Kernel and Run All Cells**. Path `data/...` relatif terhadap folder notebook. Sel pertama mencetak executable Python untuk memeriksa environment aktif. Dependensi tercantum dalam [environment.yml](environment.yml).

Untuk membuat environment baru pada perangkat lain:

```sh
conda env create -f environment.yml
```

Data CSV dan arsip gambar merupakan lampiran asli modul; URL dan SHA-256 dicatat di `data/provenance.json` masing-masing folder. Praktikum wajah menyediakan hasil `fetch_lfw_people(min_faces_per_person=60)` dalam NPZ lokal. Praktikum ANN Spotify mempertahankan seluruh 955.320 baris dan sembilan fitur numerik sebagaimana [provenance Spotify](JS06/data/provenance.json).

## Tugas Colab dan PyDroid3

[Notebook tugas ANN](JS06/Tugas_Praktikum_244107020049_Agus.ipynb), [kode Colab dengan FAISS](JS06/benchmark_colab.py), dan [kode PyDroid3 tanpa FAISS](JS06/benchmark_pydroid3.py) tersedia. Hasil kedua perangkat sudah dimasukkan ke notebook beserta spesifikasi HP Dimensity 8500 Ultra/RAM 16 GB, tabel waktu/recall, grafik, dan analisis. Berkas `JS06/hasil_colab.json` dan `JS06/hasil_android.json` ditranskripsi dari output konsol pengguna; informasi yang tidak diberikan tetap kosong. Exact NN, Annoy, dan HNSW dibandingkan lintas perangkat; FAISS hanya dicatat pada Colab. Perbedaan hash StandardScaler antar versi sudah direkonstruksi dan dibahas sebagai batas perbandingan. Petunjuk menjalankannya ada di [README ANN](JS06/README.md).
