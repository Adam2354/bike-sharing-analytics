# Bike Sharing Data Analysis

## Deskripsi Proyek
Proyek ini bertujuan untuk menganalisis pola penyewaan sepeda berdasarkan waktu, hari kerja, kondisi cuaca, dan karakteristik pengguna menggunakan Bike Sharing Dataset periode 2011–2012 di Washington D.C.

## Dataset
Dataset terdiri atas dua file utama:
- `hour.csv`: Data penyewaan sepeda per jam.
- `day.csv`: Data penyewaan sepeda per hari.

## Teknologi
- Python
- Pandas dan NumPy
- Matplotlib dan Seaborn
- Streamlit
- Jupyter Notebook

## Struktur Proyek
- `data/raw/`: Dataset asli.
- `data/cleaned/`: Dataset yang telah dibersihkan.
- `notebooks/`: Notebook analisis.
- `dashboard/`: Aplikasi dashboard.

## Menjalankan Dashboard
```bash
pip install -r requirements.txt
streamlit run dashboard/app.py
```