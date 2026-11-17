---
title: Day vs Night Classifier
emoji: 🌗
colorFrom: yellow
colorTo: indigo
sdk: docker
app_port: 7860
pinned: false
---

# Day vs Night Classifier (JS15 Praktikum 2)

Flask + Docker deployment of the HOG + neural network model from `Praktikum_1_244107020049_Agus.ipynb`.
Upload a photo on the home page; `/predict` returns `Day (Siang)` or `Night (Malam)`.

Files: `app.py`, `requirements.txt`, `Dockerfile`, `day_night_model.h5`, `scaler.pkl`.

Run locally without Docker (from this folder, using the repository `.venv`):

```sh
../../.venv/bin/python app.py   # http://localhost:7860
```

Deploy: create a Docker Space on Hugging Face, `git lfs install`, clone the Space, copy these files in, then `git add . && git commit -m "Deploy aplikasi ke HF" && git push` with a Write access token as the password.
