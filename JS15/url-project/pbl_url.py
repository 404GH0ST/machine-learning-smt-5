"""Utilitas dataset PBL Malicious URL Detection yang dipakai bersama oleh notebook JS02-JS15.

Dataset: ``Malicious URL Detection.csv`` (kolom ``url``, ``type``) di root repositori.
URL sudah dinormalisasi oleh sumbernya: huruf kecil, tanpa skema ``http(s)://`` dan tanpa ``www.``.
"""
from pathlib import Path
import math
import re

import numpy as np
import pandas as pd

DATA_PATH = Path(__file__).resolve().parent / "Malicious URL Detection.csv"
CLASSES = ["benign", "legitimate", "defacement", "phishing", "malware", "spam", "Exploit"]
BENIGN_CLASSES = {"benign", "legitimate"}

SUSPICIOUS_WORDS = ["login", "signin", "secure", "account", "update", "verify", "bank", "confirm",
                    "password", "webscr", "ebayisapi", "paypal", "free", "lucky", "bonus", "admin", "wp-"]
SHORTENERS = {"bit.ly", "goo.gl", "tinyurl.com", "ow.ly", "t.co", "is.gd", "buff.ly", "adf.ly",
              "bitly.com", "cutt.ly", "shorturl.at", "rebrand.ly", "tiny.cc", "rb.gy"}
_IPV4 = re.compile(r"^\d{1,3}(\.\d{1,3}){3}(:\d+)?$")
_EXECUTABLE = re.compile(r"\.(exe|sh|bin|apk|jar|scr|dll|mips|arm\d?|x86|ppc|m68k|spc|mpsl|sh4|i686)$")


def load_urls(path=DATA_PATH, sample=None, random_state=42):
    """Muat dataset. ``sample`` = jumlah baris yang diambil secara stratified per kelas (None = semua)."""
    df = pd.read_csv(path, dtype={"url": str, "type": str}).dropna()
    if sample is not None and sample < len(df):
        from sklearn.model_selection import train_test_split
        df, _ = train_test_split(df, train_size=sample, stratify=df["type"], random_state=random_state)
    return df.reset_index(drop=True)


def normalize_url(url):
    """Samakan format input dengan dataset: huruf kecil, tanpa skema http(s):// dan tanpa awalan www."""
    url = str(url).strip().lower()
    url = re.sub(r"^[a-z][a-z0-9+.-]*://", "", url)
    return re.sub(r"^www\d*\.", "", url)


def binary_label(types):
    """0 = aman (benign/legitimate), 1 = berbahaya (defacement, phishing, malware, spam, Exploit)."""
    return (~pd.Series(types).isin(BENIGN_CLASSES)).astype(int).to_numpy()


def _entropy(s):
    if not s:
        return 0.0
    counts = np.unique(list(s), return_counts=True)[1] / len(s)
    return float(-(counts * np.log2(counts)).sum())


def lexical_features(urls):
    """Fitur leksikal URL (Ma dkk., 2009; Mamun dkk., 2016; Sahoo dkk., 2017). Mengembalikan DataFrame numerik."""
    rows = []
    for url in urls:
        url = str(url).strip().lower()
        host, _, rest = url.partition("/")
        path, _, query = rest.partition("?")
        hostname = host.split(":")[0]
        labels = [p for p in hostname.split(".") if p]
        filename = path.rsplit("/", 1)[-1]
        digits = sum(ch.isdigit() for ch in url)
        letters = sum(ch.isalpha() for ch in url)
        rows.append({
            "url_len": len(url),
            "host_len": len(hostname),
            "path_len": len(path),
            "query_len": len(query),
            "n_dots": url.count("."),
            "n_hyphens": url.count("-"),
            "n_underscores": url.count("_"),
            "n_slashes": url.count("/"),
            "n_question": url.count("?"),
            "n_equals": url.count("="),
            "n_ampersand": url.count("&"),
            "n_at": url.count("@"),
            "n_percent": url.count("%"),
            "n_digits": digits,
            "digit_ratio": digits / max(len(url), 1),
            "letter_ratio": letters / max(len(url), 1),
            "n_subdomains": max(len(labels) - 2, 0),
            "tld_len": len(labels[-1]) if labels else 0,
            "path_depth": path.count("/") + (1 if path else 0),
            "is_ip": int(bool(_IPV4.match(host))),
            "has_port": int(":" in host),
            "is_shortener": int(hostname in SHORTENERS),
            "n_suspicious_words": sum(w in url for w in SUSPICIOUS_WORDS),
            "has_executable_ext": int(bool(_EXECUTABLE.search(filename))),
            "has_php": int(".php" in path),
            "has_html": int(".htm" in path),
            "entropy": _entropy(url),
            "host_entropy": _entropy(hostname),
        })
    return pd.DataFrame(rows)


FEATURE_NAMES = list(lexical_features(["example.com/a?b=c"]).columns)
