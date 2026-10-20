"""Benchmark JS06 untuk PyDroid3 Android: Exact NN, Annoy, dan HNSW."""
import hashlib
import importlib.metadata
import json
import os
import platform
from pathlib import Path
import sys

# Isi model HP/chipset untuk PyDroid3; Colab boleh dibiarkan kosong.
DEVICE = ""
OUTPUT = "hasil_android.json"


def recall_at_k(pred, truth, k):
    return sum(len(set(a[:k]) & set(b[:k])) for a, b in zip(pred, truth)) / (len(truth) * k)


def run_benchmark(device=DEVICE, output=OUTPUT, label="android"):
    import numpy as np
    import time
    from sklearn.neighbors import NearestNeighbors
    from annoy import AnnoyIndex
    import hnswlib
    from sklearn.preprocessing import StandardScaler

    # -------------------------------
    # Contoh dataset kecil untuk testing
    # -------------------------------
    np.random.seed(42)
    n_samples = 10000   # jumlah database vector
    d = 128             # dimensi
    X = np.random.random((n_samples, d)).astype('float32')

    # Standarisasi fitur
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    k = 10  # jumlah nearest neighbors

    # -------------------------------
    # Exact NN (brute-force)
    # -------------------------------
    start = time.time()
    nn = NearestNeighbors(n_neighbors=k, algorithm='brute', metric='euclidean')
    nn.fit(X_scaled)
    dist_exact, idx_exact = nn.kneighbors(X_scaled)
    time_exact = time.time() - start
    print(f"Exact NN done in {time_exact:.3f} s")

    # -------------------------------
    # Annoy
    # -------------------------------
    start = time.time()
    f = X_scaled.shape[1]
    index_annoy = AnnoyIndex(f, 'euclidean')
    for i, v in enumerate(X_scaled):
        index_annoy.add_item(i, v)
    index_annoy.build(10)
    idx_annoy = [index_annoy.get_nns_by_vector(v, k) for v in X_scaled]
    time_annoy = time.time() - start
    print(f"Annoy done in {time_annoy:.3f} s")

    # -------------------------------
    # HNSW
    # -------------------------------
    start = time.time()
    p_hnsw = hnswlib.Index(space='l2', dim=d)
    p_hnsw.init_index(max_elements=n_samples, ef_construction=200, M=16)
    p_hnsw.add_items(X_scaled)
    p_hnsw.set_ef(200)
    idx_hnsw, _ = p_hnsw.knn_query(X_scaled, k=k)
    time_hnsw = time.time() - start
    print(f"HNSW done in {time_hnsw:.3f} s")

    if any(len(neighbors) != k for neighbors in idx_annoy):
        raise RuntimeError('Annoy tidak mengembalikan k tetangga; hasil benchmark belum valid.')

    seconds = {'Exact NN': time_exact, 'Annoy': time_annoy, 'HNSW': time_hnsw}
    recall = {'Exact NN': 1.0, 'Annoy': recall_at_k(idx_annoy, idx_exact, k), 'HNSW': recall_at_k(idx_hnsw, idx_exact, k)}
    versions = {}
    for package in ['numpy', 'scikit-learn', 'annoy', 'hnswlib']:
        try:
            versions[package] = importlib.metadata.version(package)
        except importlib.metadata.PackageNotFoundError:
            versions[package] = 'unknown'
    try:
        import psutil
        ram_gib = psutil.virtual_memory().total / 1024**3
    except ImportError:
        ram_gib = None

    result = {
        'label': label,
        'device': device,
        'environment': {'python': sys.version, 'platform': platform.platform(),
                        'machine': platform.machine(), 'cpu': platform.processor(),
                        'logical_cpus': os.cpu_count(), 'ram_gib': ram_gib,
                        'versions': versions},
        'parameters': {'n_samples': n_samples, 'dimensions': d, 'k': k, 'annoy_trees': 10, 'hnsw_M': 16, 'hnsw_ef_construction': 200, 'hnsw_ef': 200},
        'data_sha256': hashlib.sha256(X_scaled.tobytes()).hexdigest(),
        'timing_scope': 'index construction plus all database rows as queries',
        'seconds': seconds,
        'recall_at_10': recall,
        'first_query_neighbors': {'Exact NN': idx_exact[0].tolist(), 'Annoy': idx_annoy[0], 'HNSW': idx_hnsw[0].tolist()},
    }
    print('\n=== Ringkasan: build + query seluruh data ===')
    for name in seconds:
        print(f'{name:10s}: {seconds[name]:.3f} s | Recall@10: {recall[name]:.4f}')
    print('\nPerangkat:', device or platform.machine())
    print('Platform:', platform.platform())
    print('RAM (GiB):', ram_gib)
    print('Versi library:', versions)
    print('Parameter:', result['parameters'])
    print('SHA-256 data:', result['data_sha256'])
    output = Path(output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2), encoding='utf-8')
    print('Hasil tersimpan:', output.resolve())
    return result


if __name__ == "__main__":
    run_benchmark()
