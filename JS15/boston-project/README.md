---
title: Boston House Price
emoji: 🏠
colorFrom: blue
colorTo: green
sdk: docker
app_port: 7860
pinned: false
---

# Boston House Price Predictor (JS15 Tugas)

Flask + Docker deployment of the MLP regression model (Dense 64-32-1) from JS13 Praktikum 3, retrained in `Tugas_Praktikum_244107020049_Agus.ipynb`.
Fill in the 13 Boston Housing features; `/predict` returns the estimated median home value in thousands of USD.

Files: `app.py`, `requirements.txt`, `Dockerfile`, `boston_model.h5`, `scaler.pkl`.

Run locally without Docker: `../../.venv/bin/python app.py`, then open http://localhost:7860.
