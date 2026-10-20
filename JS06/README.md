# JS06 - Approximate Nearest Neighbors

Praktikum 1–6 mengikuti [modul GitBook](https://polinema.gitbook.io/jti-modul-praktikum-pembelajaran-mesin-2025-2026/js06-ann-approximate-nearest-neighbors), termasuk tabel percobaan tambahan dan analisis. Buka notebook dari folder `JS06` agar path data sesuai.

Praktikum 1 memakai 1 juta track sintetis sesuai tabel modul; contoh kode pada halaman menulis 50 juta. Praktikum 6 memakai seluruh baris dataset nyata dengan sembilan fitur numerik yang sama. Sumber dan hash data tersedia di [data/README.md](data/README.md). Constructor FAISS pada Praktikum 6 dan tugas memakai argumen posisi karena keyword `nlist` menghasilkan `TypeError` pada versi yang diuji.

## Lingkungan verifikasi lokal

Notebook diuji pada Python 3.11 di environment `ml-praktikum`. Build standar Annoy 1.17.3 pada macOS ARM64 dengan Apple Clang 21 mengembalikan hanya satu atau dua tetangga meskipun diminta sepuluh. Build tanpa `-ffast-math` memperbaiki hasil pada lingkungan ini; [laporan upstream](https://github.com/spotify/annoy/issues/686) menjelaskan gejala serupa. Kode pencarian dari modul tidak diubah.

Jika memakai lingkungan macOS yang sama, perintah build yang diverifikasi adalah:

```sh
ANNOY_COMPILER_ARGS="-O3,-fno-fast-math,-DANNOYLIB_MULTITHREADED_BUILD,-std=c++14" python -m pip install --force-reinstall --no-cache-dir --no-binary=annoy --no-deps annoy==1.17.3
```

Pengaturan build ini memengaruhi hasil waktu benchmark lokal. Hasil Colab dan smartphone tetap diukur pada lingkungan masing-masing.

## Tugas Colab dan PyDroid3

Kode tersedia dalam [notebook tugas](Tugas_Praktikum_244107020049_Agus.ipynb), [script mandiri Colab](benchmark_colab.py), dan [script mandiri PyDroid3](benchmark_pydroid3.py). Hasil Colab dan smartphone dari output konsol pengguna sudah dimasukkan ke notebook beserta spesifikasi HP Dimensity 8500 Ultra/RAM 16 GB. Kode utama tetap memakai data, parameter, dan urutan algoritma pada modul.

**Google Colab tetap memakai FAISS**, bersama Exact NN, Annoy, dan HNSW. Jalankan instalasi di satu sel:

```python
%pip install -q numpy scikit-learn annoy hnswlib faiss-cpu psutil
```

Kemudian salin seluruh isi `benchmark_colab.py` ke sel berikutnya dan jalankan. Jika mengunggah file Python tersebut melalui panel Files, jalankan:

```python
%run benchmark_colab.py
```

Output disimpan sebagai `hasil_colab.json`; unduh melalui panel Files.

**PyDroid3 tanpa FAISS:** pasang dependensi berikut melalui terminal/Pip PyDroid3:

```sh
pip install numpy scikit-learn annoy hnswlib
```

Salin `benchmark_pydroid3.py` ke editor, isi `DEVICE` dengan model HP/chipset yang sebenarnya, simpan, dan tekan Run. Kode tidak mengimpor atau menjalankan FAISS. `psutil` opsional untuk mencatat RAM; tanpa paket itu, isi RAM bernilai `null` dan spesifikasi dapat ditulis manual. Output disimpan sebagai `hasil_android.json` pada direktori kerja yang dicetak di akhir program.

Kedua script dapat dijalankan sendiri tanpa file pendamping. Gunakan `benchmark_colab.py` untuk Google Colab dan `benchmark_pydroid3.py` untuk PyDroid3.

Setiap JSON mencatat waktu build + query seluruh data, recall, versi library, hash input, serta informasi lingkungan. Gunakan dataset dan parameter yang sama pada kedua perangkat. Notebook tugas memvalidasi parameter bersama, merekonstruksi perbedaan hash, dan membandingkan Exact NN, Annoy, dan HNSW. Saat laporan dijalankan secara lokal, `RUN_BENCHMARK=False` menjaga kedua hasil perangkat agar tidak tertimpa benchmark lokal. FAISS dicatat hanya pada Colab; pada Android ditandai tidak dijalankan, tanpa rasio waktu lintas perangkat.

Pemanggilan indeks mengacu pada dokumentasi resmi [Annoy](https://github.com/spotify/annoy), [HNSW](https://github.com/nmslib/hnswlib), dan [FAISS](https://github.com/facebookresearch/faiss/wiki/Getting-started).


## Hasil perangkat yang diberikan pengguna

| Model | Colab total (s) | PyDroid3 total (s) | Recall Colab | Recall PyDroid3 |
| --- | ---: | ---: | ---: | ---: |
| Exact NN | 3.195 | 0.557 | 1.0000 | 1.0000 |
| Annoy | 1.475 | 0.918 | 0.1678 | 0.1681 |
| HNSW | 12.189 | 4.689 | 0.9805 | 0.9806 |
| FAISS IVF | 0.376 | Tidak dijalankan | 0.4182 | Tidak dijalankan |

Waktu mencakup build index + seluruh query. Pada run ini, waktu total di HP lebih singkat dengan rasio Colab/PyDroid3 sekitar 5,74× untuk Exact NN, 1,61× untuk Annoy, dan 2,60× untuk HNSW. Colab memakai scikit-learn 1.6.1/NumPy 2.1.3, sedangkan Android 1.8.0/2.4.4; hasil tidak mengisolasi pengaruh perangkat keras.

[Hasil Colab](hasil_colab.json) dan [hasil Android](hasil_android.json) merupakan transkripsi output konsol, bukan JSON asli yang diunggah. Hasil tersedia dengan presisi waktu tiga angka desimal dan recall empat angka desimal. Versi Python/model CPU Colab/jumlah thread tidak diberikan. RAM HP 16 GB berasal dari pengguna, sedangkan RAM terbaca psutil 11,094 GiB dicatat terpisah.

Kedua hash berbeda karena pembulatan StandardScaler float32 antar versi. Rekonstruksi lokal berhasil menghasilkan kedua hash persis dengan selisih nilai maksimum sekitar 3,58×10⁻⁷; bukti tersimpan pada [hasil_verifikasi_hash.json](hasil_verifikasi_hash.json) dan notebook tugas. Data tidak identik byte, sehingga tabel merupakan perbandingan deskriptif. Sumber perubahan operasi dapat dilihat pada [kode scikit-learn 1.6.1](https://github.com/scikit-learn/scikit-learn/blob/1.6.1/sklearn/preprocessing/_data.py) dan [1.8.0](https://github.com/scikit-learn/scikit-learn/blob/1.8.0/sklearn/preprocessing/_data.py).
