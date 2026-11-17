---
title: Malicious URL Detector
emoji: 🛡️
colorFrom: red
colorTo: gray
sdk: docker
app_port: 7860
pinned: false
---

# Malicious URL Detector (PBL JS15)

Flask + Docker deployment of the neural network trained in `PBL_Malicious_URL_244107020049_Agus.ipynb` on the PBL *Malicious URL Detection* dataset.
Enter a URL; `/predict` returns one of `benign`, `legitimate`, `defacement`, `phishing`, `malware`, `spam`, `Exploit` with class probabilities.

Files: `app.py`, `pbl_url.py` (same feature extraction used in training), `labels.json`, `url_model.h5`, `scaler.pkl`, `requirements.txt`, `Dockerfile`.

Run locally: `../../.venv/bin/python app.py`, then open http://localhost:7860.
