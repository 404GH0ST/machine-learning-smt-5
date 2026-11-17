# Praktikum Pembelajaran Mesin

Nama: **Agus** · NIM: **244107020049**

Pengerjaan modul [GitBook Polinema 2025/2026](https://polinema.gitbook.io/jti-modul-praktikum-pembelajaran-mesin-2025-2026). Notebook menggunakan kernel **Python (Miniconda ml-praktikum)**. Kode utama praktikum mengikuti urutan dan blok kode modul; penyesuaian kompatibilitas dijelaskan pada notebook masing-masing. Evaluasi tambahan diletakkan setelah langkah modul.

| Modul | Folder | Praktikum | Tugas |
| --- | --- | --- | --- |
| JS05 Klasterisasi Hierarki | [JS05](JS05/) | 1–2: HDBSCAN, eksperimen parameter, evaluasi | HDBSCAN pada Iris |
| JS06 Approximate Nearest Neighbors | [JS06](JS06/) | 1–6: Annoy, FAISS, HNSW, recall/QPS, Spotify | Perbandingan Colab/PyDroid3, spesifikasi HP, dan analisis hasil |
| JS06 Regresi | [JS06_Regresi](JS06_Regresi/) | 1: OLS; 2: SVR | Multiple Linear Regression biaya medis |
| JS09 Klasifikasi | [JS09](JS09/) | 1: kNN; 2–3: Naive Bayes | 1: fitur/k suara; 2: CountVectorizer vs TF-IDF |
| JS11 Klasifikasi 2 | [JS11](JS11/) | 1–3: SVM sintetis; 4: wajah; 5: siang/malam | SVM suara dan histogram HSV siang/malam |
| JS13 ANN dan Evaluasi Classifier | [JS13](JS13/) | 1: JST manual XOR; 2: Keras Iris; 3: regresi dummy dan Boston | JST MNIST: neuron, layer, waktu, Sigmoid vs ReLU |
| JS14 CNN | [JS14](JS14/) | 1: cat vs dog; 2: CIFAR-10; tambahan: CNN teks (IMDB, 20 Newsgroups) | CIFAR-10 > 80% dan CNN MNIST |
| JS15 Pipeline & Deployment | [JS15](JS15/) | 1: Day vs Night HOG + NN; 2: Flask + Docker untuk Hugging Face | Deploy MLP harga rumah Boston |

JS05–JS11 berisi **24 notebook (18 praktikum dan 6 tugas)** yang divalidasi di Jupyter Miniconda. JS13–JS15 menambah **11 notebook (7 praktikum, 1 eksperimen CNN teks, dan 3 tugas)** yang dijalankan di `.venv`. Semua notebook menyimpan output. Notebook tugas ANN mengolah hasil Colab/PyDroid3 yang dikirim pengguna; angka pengukuran perangkat tidak diganti dengan benchmark lokal. Dua modul bernomor JS06 dipisahkan agar ANN dan regresi tidak saling menimpa. File menggunakan pola `Praktikum_N_244107020049_Agus.ipynb` dan `Tugas_Praktikum_244107020049_Agus.ipynb`; JS09 memiliki `Tugas_1` dan `Tugas_2`.

## PBL - Malicious URL Detection

Dataset PBL `Malicious URL Detection.csv` (783.705 URL; kelas `benign`, `phishing`, `defacement`, `malware`, `legitimate`, `spam`, `Exploit`) diterapkan pada setiap jobsheet yang dapat memakainya. Setiap folder berisi `PBL_Malicious_URL_244107020049_Agus.ipynb`. Fungsi muat data, normalisasi URL, dan 28 fitur leksikal ada di [`pbl_url.py`](pbl_url.py), sehingga semua notebook dan aplikasi deploy memakai definisi fitur yang sama.

| Jobsheet | Penerapan pada URL |
| --- | --- |
| [JS02](JS02/PBL_Malicious_URL_244107020049_Agus.ipynb) | EDA, outlier, korelasi, missing/duplikat, encoding, standardisasi, tokenisasi URL |
| [JS03](JS03/PBL_Malicious_URL_244107020049_Agus.ipynb) | Ekstraksi fitur leksikal, seleksi fitur (F/MI), random vs stratified split, CV, BoW vs TF-IDF n-gram karakter |
| [JS04](JS04/PBL_Malicious_URL_244107020049_Agus.ipynb) | KMeans (elbow, silhouette), MiniBatchKMeans seluruh data, DBSCAN |
| [JS05](JS05/PBL_Malicious_URL_244107020049_Agus.ipynb) | HDBSCAN vs DBSCAN, scale invariance, `min_cluster_size`/`min_samples`, silhouette dan DBI |
| [JS06](JS06/PBL_Malicious_URL_244107020049_Agus.ipynb) | Pencarian URL mirip: exact, Annoy, FAISS IVF/PQ, HNSW (recall, QPS, kNN) |
| [JS09](JS09/PBL_Malicious_URL_244107020049_Agus.ipynb) | kNN (k dan jumlah fitur), GaussianNB, MultinomialNB/ComplementNB dengan Count vs TF-IDF |
| [JS11](JS11/PBL_Malicious_URL_244107020049_Agus.ipynb) | SVM enam kombinasi split/kernel, pengaruh C, GridSearch, LinearSVC TF-IDF seluruh data |
| [JS13](JS13/PBL_Malicious_URL_244107020049_Agus.ipynb) | MLP Keras, evaluasi classifier lengkap (CM, ROC), arsitektur, aktivasi, class weight |
| [JS14](JS14/PBL_Malicious_URL_244107020049_Agus.ipynb) | CNN level karakter (pola modul dan multi-kernel ala eXpose) vs TF-IDF + LinearSVC |
| [JS15](JS15/PBL_Malicious_URL_244107020049_Agus.ipynb) | Pipeline dan deploy Flask + Docker di [JS15/url-project](JS15/url-project/) |

Tidak dipakai di **JS01** (instalasi environment dan esai etika, tanpa pengolahan data) dan **JS06 Regresi** (dataset tidak memiliki target kontinu).

## Environment JS13–JS15 (`.venv`)

Mulai JS13, notebook memakai `.venv` di root repositori (Python 3.12, TensorFlow 2.21, CPU), bukan environment Miniconda. GPU Apple M4 lewat `tensorflow-metal` 1.2.0 (versi terbaru, hanya mendukung TensorFlow 2.18) sudah dicoba. Training memang sekitar 1,85× lebih cepat, tetapi hasilnya salah: MLP MNIST yang di CPU mencapai 96,9% hanya mendapat 74% di GPU, dan dengan SGD akurasinya kolaps ke 0%. Karena itu semua notebook dijalankan di CPU.

```sh
uv venv --python 3.12 && uv pip install -r requirements.txt
.venv/bin/jupyter lab        # pilih kernel Python 3 (.venv)
```

Sesuai arahan dosen, JS13–JS15 mengikuti langkah dan dataset jobsheet. Perbandingan model dirujuk ke jurnal, dan CNN juga dicoba pada data teks (JS14).

## Menjalankan di Jupyter Miniconda (JS05–JS11)

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
