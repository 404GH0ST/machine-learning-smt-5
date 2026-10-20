# Data Micro Spotify

Sumber: [dataset Kaggle pada modul](https://www.kaggle.com/datasets/bwandowando/spotify-songs-with-attributes-and-lyrics), versi 20.
File pertama: `songs_with_attributes_and_lyrics.csv`.

`spotify_songs.csv.gz` berisi seluruh **955,320 baris** dalam urutan asli,
dengan sembilan fitur numerik yang digunakan pada kode Praktikum 6:
danceability, energy, loudness, speechiness, acousticness, instrumentalness, liveness, valence, tempo.

Tidak ada sampling, penghapusan baris, atau normalisasi saat menyiapkan file.
StandardScaler dijalankan di notebook. Kolom metadata dan lirik tidak disertakan
karena tidak masuk ke perhitungan jarak. Pandas membaca gzip langsung melalui
`pd.read_csv('data/spotify_songs.csv.gz')`.

Ukuran file sumber adalah 1,545,144,675 byte. Hash arsip unduhan, CRC32
file sumber, dan SHA-256 proyeksi dicatat di [provenance.json](provenance.json).
