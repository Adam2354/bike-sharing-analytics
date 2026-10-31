# Bike Sharing Data Analysis

## 📊 Deskripsi Proyek

Proyek ini merupakan analisis data penyewaan sepeda (*Bike Sharing*) di Washington D.C. selama periode 2011–2012. Analisis dilakukan untuk memahami pola dan karakteristik penyewaan sepeda berdasarkan waktu, hari kerja, kondisi cuaca, serta tipe pengguna.

Melalui proses *data analysis*, proyek ini bertujuan untuk memperoleh informasi mengenai tren penyewaan sepeda, waktu dengan tingkat permintaan tertinggi, pengaruh kondisi cuaca, dan perbedaan perilaku antara pengguna *casual* dan *registered*.

## 🌐 Dashboard Online

Dashboard interaktif hasil analisis dapat diakses melalui tautan berikut:

### [🚴 Bike Sharing Analytics Dashboard](https://bike-sharing-analytics-elisia.streamlit.app/)

Dashboard dikembangkan menggunakan Streamlit dan menyediakan visualisasi data serta fitur filter interaktif untuk mengeksplorasi pola penyewaan sepeda berdasarkan berbagai kategori.

## 🎯 Pertanyaan Bisnis

Analisis ini berfokus pada empat pertanyaan bisnis:

1. Bagaimana perkembangan jumlah penyewaan sepeda harian selama Januari 2011 hingga Desember 2012, dan bulan apa yang memiliki rata-rata penyewaan harian tertinggi?
2. Pada jam berapa penyewaan sepeda mencapai puncaknya, dan bagaimana perbedaan pola penyewaan antara hari kerja dan hari non-kerja?
3. Bagaimana perbedaan rata-rata jumlah penyewaan sepeda berdasarkan empat kategori kondisi cuaca?
4. Bagaimana kontribusi pengguna *casual* dan *registered* berbeda pada setiap musim?

## 📁 Dataset

Dataset yang digunakan adalah **Bike Sharing Dataset** dengan periode pengamatan tahun 2011–2012 di Washington D.C.

Dataset terdiri atas dua file utama:

- `hour.csv`: Data penyewaan sepeda berdasarkan jam.
- `day.csv`: Data penyewaan sepeda berdasarkan hari.

Dataset mencakup informasi tanggal, waktu, musim, kondisi cuaca, temperatur, kelembapan, kecepatan angin, serta jumlah penyewaan sepeda dari pengguna *casual* dan *registered*.

## 🛠️ Teknologi dan Tools

Teknologi dan library yang digunakan dalam proyek ini meliputi:

- **Python** – Bahasa pemrograman untuk analisis data.
- **Pandas** – Pengolahan dan manipulasi data.
- **NumPy** – Komputasi numerik.
- **Matplotlib** – Visualisasi data.
- **Seaborn** – Visualisasi statistik.
- **Streamlit** – Pengembangan dashboard interaktif.
- **Jupyter Notebook** – Dokumentasi dan pelaksanaan proses analisis data.

## 🔄 Tahapan Analisis Data

Proyek ini dilaksanakan melalui beberapa tahapan:

1. **Data Gathering** – Mengumpulkan dan memuat dataset `hour.csv` dan `day.csv`.
2. **Data Assessing** – Memeriksa kualitas data, tipe data, missing values, dan duplikasi.
3. **Data Cleaning** – Melakukan perbaikan tipe data dan penanganan data sesuai hasil pemeriksaan.
4. **Exploratory Data Analysis (EDA)** – Mengeksplorasi pola penyewaan sepeda berdasarkan waktu, cuaca, musim, dan tipe pengguna.
5. **Data Visualization** – Menyajikan hasil analisis dalam bentuk visualisasi untuk menjawab pertanyaan bisnis.
6. **Conclusion and Recommendation** – Menyusun kesimpulan dan rekomendasi berdasarkan hasil analisis.

## 📂 Struktur Direktori Proyek

```text
bike-sharing-analytics/
│
├── dashboard/
│   └── app.py
│
├── data/
│   ├── raw/
│   │   ├── hour.csv
│   │   ├── day.csv
│   │   └── Readme.txt
│   │
│   └── cleaned/
│       ├── hour_cleaned.csv
│       └── day_cleaned.csv
│
├── notebooks/
│   └── Proyek_Analisis_Data_Elisia_Nurin.ipynb
│
├── README.md
├── requirements.txt
└── url.txt
```

## 💻 Cara Menjalankan Proyek Secara Lokal

Ikuti langkah berikut untuk menjalankan dashboard di komputer lokal.

**1. Clone repository**

```bash
git clone https://github.com/Adam2354/bike-sharing-analytics.git
```

**2. Masuk ke direktori proyek**

```bash
cd bike-sharing-analytics
```

**3. Instal dependencies**

```bash
pip install -r requirements.txt
```

**4. Jalankan aplikasi Streamlit**

```bash
streamlit run dashboard/app.py
```

Setelah berhasil dijalankan, dashboard dapat diakses melalui alamat lokal yang ditampilkan di terminal, biasanya `http://localhost:8501`.

## 📌 Hasil Proyek

Hasil dari proyek ini meliputi:

- Notebook analisis data yang mendokumentasikan proses pengolahan dan eksplorasi data.
- Visualisasi untuk menjawab pertanyaan bisnis.
- Dashboard interaktif berbasis Streamlit.
- Kesimpulan dan rekomendasi berdasarkan hasil analisis.

## 📚 Referensi Dataset

Fanaee-T, H., & Gama, J. (2013). Event labeling combining ensemble detectors and background knowledge. *Progress in Artificial Intelligence*, 2, 113–127.

https://doi.org/10.1007/s13748-013-0040-3

---

**Bike Sharing Data Analysis Project**  
Dashboard: https://bike-sharing-analytics-elisia.streamlit.app/