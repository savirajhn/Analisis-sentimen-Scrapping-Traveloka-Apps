# -*- coding: utf-8 -*-
"""Scrapping Traveloka.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1x8RO2atUhUgjMTeQJw9xF6bacRnVqbqD
"""

import pandas as pd
from google_play_scraper import reviews_all, Sort

# Scraping reviews dari aplikasi Traveloka
traveloka_reviews = reviews_all(
    'com.traveloka.android',  # ID aplikasi Traveloka
    lang='id',                # Bahasa Indonesia
    country='id',             # Indonesia
    sort=Sort.NEWEST,         # Urutkan dari yang terbaru
    count=3500,               # Jumlah review yang diambil
    filter_score_with=None    # Ambil semua rating
)

# Convert ke DataFrame
df = pd.DataFrame(traveloka_reviews)

# Simpan ke CSV
df.to_csv('traveloka_reviews.csv', index=False)

# Tampilkan 5 data teratas
print(df.head())