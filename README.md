# Credit-Scoring-Analytics
# Menyelesaikan Permasalahan Perusahaan Finance Merdeka untuk menentukan Nasabah mereka memiliki credit score good, standard atau poor.

## Bussiness Understanding
By definition, credit scoring analytics merupakan sebuah proses analisis yang dilakukan oleh pemberi pinjaman (lenders) atau institusi keuangan guna menentukan kelayakan kredit (creditworthiness) dari peminjam (borrower). Proses ini biasanya akan menghasilkan sebuah nilai numerik yang menentukan kemungkinan peminjam tersebut gagal bayar. Nilai numerik inilah yang menjadi acuan pemberi pinjaman dalam menilai resiko dari sebuah kredit.
Finance Merdeka merupakan sebuah perusahaan teknologi baru yang bergerak di bidang keuangan. Ia menyediakan berbagai solusi keuangan berbasis teknologi untuk memberdayakan individu dan pelaku usaha.
Setelah beroperasi selama satu tahun, Finance Merdeka telah mengumpulkan data yang berkaitan dengan keadaan keuangan dan kredit dari seluruh pelanggan. Nah, sebagai seorang data scientist, Anda diminta untuk memanfaatkan data tersebut guna mengoptimalkan proses pemeriksaan risiko kredit ketika pengajuan pinjaman berlangsung.

## Bussiness Problem
Walaupun menyediakan berbagai solusi keuangan berbasis teknologi, terdapat beberapa tahapan dalam layanan tersebut yang dilakukan secara manual. Salah satu tahapan tersebut ialah pemeriksaan risiko kredit ketika individu dan pelaku usaha mengajukan pinjaman. Tahapan ini sepenuhnya dilakukan secara manual oleh tim Risk Analytics Analyst. Tahapan ini tentunya memakan banyak waktu dan sangat tidak efisien. Oleh karena itu, Finance Merdeka berupaya untuk mengoptimalkan tahapan tersebut.

## Project Scope
- Melakukan tahap awal data preparation dan data cleaning.
- Melaksanakan Exploratory Data Analysis (EDA) untuk mengidentifikasi faktor-faktor yang berkontribusi terhadap nasabah  memiliki credit score good, standard atau poor melalui visualisasi data.
- Mengembangkan model machine learning guna memprediksi status nasabah berdasarkan variabel-variabel yang menjadi penyebab memiliki credit score good, standard atau poor.
- Melakukan deployment model machine learning agar dapat digunakan untuk memprediksi apakah seorang nasabah memiliki credit score good, standard atau poor.

## Preparation
***Data Source***
- [Credit Score Classification Dataset](https://www.kaggle.com/datasets/parisrohan/credit-score-classification)

## Setup Environment - Anaconda

1. Clone Repository
   ```bash
   git clone https://github.com/RozyRangkuti/Credit-Scoring-Analytics.git
   ```

2. Buka Terminal Anaconda, jalankan perintah berikut untuk membuat environment baru
   ```bash
   conda create --name myenv python=3.11
   ```
   
3. Aktifkan virtual environment dengan menjalankan perintah berikut ini
   ```bash
   conda activate myenv
   ```
   
4. Install semua requirements di dalam file "requirements.txt"
   ```bash
   pip install -r requirements.txt

   ## Machine Learning Prediction System
Untuk mendukung Perusahaan Finance Merdeka untuk memprediksi nasabah tersebut memiliki credit score good, standard atau poor, telah dikembangkan sebuah sistem prediksi. Sistem ini dibangun menggunakan platform Streamlit. Untuk menjalankan aplikasi ini secara lokal, pengguna dapat menjalankan perintah berikut di Terminal:

```bash
streamlit run credit_scoring_app.py
```

Sementara itu, untuk menghentikan aplikasi Streamlit yang sedang berjalan, cukup tekan Ctrl + C pada Terminal.

Sistem prediksi tersebut juga tersedia secara online dan dapat diakses langsung melalui tautan yang telah di-deploy ke Streamlit Cloud pada link berikut ini: https://credit-scoring-analytics.streamlit.app/
