# Proyek Akhir: Analisis dan Prediksi Tingkat Dropout Mahasiswa

## Latar Belakang

Jaya Jaya Institut, sebuah institusi pendidikan terkemuka, menghadapi tantangan signifikan terkait tingginya angka mahasiswa yang tidak menyelesaikan studi (*dropout*). Masalah ini tidak hanya berdampak pada reputasi institusi tetapi juga pada kesinambungan finansial dan moral akademik.

Untuk mengatasi masalah ini, proyek ini dikembangkan dengan dua tujuan utama:
1.  **Menganalisis faktor-faktor kunci** yang paling berpengaruh terhadap status kelulusan mahasiswa.
2.  **Membangun solusi Machine Learning** yang dapat memprediksi mahasiswa berisiko *dropout* secara dini, memungkinkan institusi untuk melakukan intervensi yang tepat sasaran.

Proyek ini mencakup analisis data eksploratif, pembangunan model prediktif, hingga implementasi dalam bentuk aplikasi web interaktif dan *dashboard* analisis.

## Struktur Proyek

Berikut adalah struktur direktori dari proyek ini:

```
submission/
├── app.py                  # Halaman utama aplikasi Streamlit
├── model/
│   ├── model_rf.pkl        # File model Machine Learning (Random Forest)
│   ├── scaler.pkl          # File scaler untuk data
│   └── label_encoder.pkl   # File encoder untuk target
├── pages/
│   ├── 1_Analisis_Data.py  # Halaman untuk dashboard analisis data
│   └── 2_Prediksi_Mahasiswa.py # Halaman untuk prediksi interaktif
├── notebook.ipynb          # Notebook Jupyter berisi semua proses analisis dan modeling
├── requirements.txt        # Daftar library yang dibutuhkan
├── README.md               # Dokumentasi proyek (file ini)
├── ashim_izzuddin-dashboard.png # Screenshot dashboard Looker Studio
├── ashim_izzuddin-video.mp4 # Video penjelasan dashboard Looker Studio
|── data_untuk_dashboard.csv # Data untuk looker studio
```

## Teknologi yang Digunakan

* **Bahasa Pemrograman:** Python 3.9
* **Analisis & Manipulasi Data:** Pandas, NumPy
* **Visualisasi Data:** Matplotlib, Seaborn
* **Machine Learning:** Scikit-learn
* **Aplikasi Web & Dashboard:** Streamlit
* **Dashboard Eksternal:** Google Looker Studio

---

## Hasil Proyek

### 1. Dashboard Analisis - Google Looker Studio

Sebuah *dashboard* interaktif telah dibuat menggunakan Google Looker Studio untuk memberikan *insight* visual mengenai data mahasiswa. *Dashboard* ini menampilkan metrik-metrik kunci dan menyoroti faktor-faktor penting yang mempengaruhi tingkat kelulusan.

**Screenshot Dashboard:**
![Dashboard Looker Studio](https://raw.githubusercontent.com/Koerentji/Menyelesaikan-Permasalahan-Institusi-Pendidikan/0af7852db2b2111d7367b6d3c778a0ea37d6cd4f/ashim_izzuddin-dashboard.png)

**Link untuk mengakses dashboard:**
**[Buka Dashboard Interaktif](https://lookerstudio.google.com/reporting/70910924-e8f1-4eab-88bb-d578a24dc2ee)**

### 2. Aplikasi Prediksi Interaktif - Streamlit

Sebuah aplikasi web multi-halaman dibangun menggunakan Streamlit untuk dua tujuan:
1.  **Halaman Analisis Data:** Menampilkan kembali visualisasi dan *insight* utama dari analisis data eksploratif.
2.  **Halaman Prediksi Mahasiswa:** Menyediakan antarmuka bagi pengguna (misalnya, staf akademik) untuk memasukkan data seorang mahasiswa dan secara instan mendapatkan prediksi status kelulusan mereka (`Graduate`, `Dropout`, atau `Enrolled`) beserta tingkat probabilitasnya.

**Link untuk mengakses streamlit:**
**[Buka Streamlit](https://menyelesaikan-permasalahan-institusi-pendidikan-uwdfjtcyfwbqr7.streamlit.app/)**

### 3. Model Machine Learning

Model klasifikasi **Random Forest** menunjukkan performa yang seimbang, terutama dalam mengidentifikasi kelas minoritas, dengan akurasi keseluruhan sekitar **76.4%**. Fitur-fitur terpenting yang digunakan oleh model antara lain adalah jumlah SKS yang disetujui dan nilai rata-rata pada dua semester pertama, serta status pembayaran SPP.

---

## Cara Menjalankan Proyek Secara Lokal

Untuk menjalankan aplikasi Streamlit secara lokal, ikuti langkah-langkah berikut:

1.  **Prasyarat:**
    * Pastikan Python 3.9 (atau versi yang sesuai) terinstal.
    * Pastikan Git terinstal.

2.  **Clone atau Unduh Proyek:**
    ```bash
    git clone [https://github.com/Koerentji/Menyelesaikan-Permasalahan-Institusi-Pendidikan.git](https://github.com/Koerentji/Menyelesaikan-Permasalahan-Institusi-Pendidikan.git)
    cd Menyelesaikan-Permasalahan-Institusi-Pendidikan
    ```

3.  **Buat dan Aktifkan Lingkungan Virtual:**
    * Ini sangat disarankan untuk menghindari konflik dependensi.
    ```bash
    # Membuat environment
    python -m venv venv

    # Mengaktifkan environment (Windows)
    venv\Scripts\activate

    # Mengaktifkan environment (macOS/Linux)
    source venv/bin/activate
    ```

4.  **Instal Dependensi:**
    * Instal semua *library* yang dibutuhkan dari file `requirements.txt`.
    ```bash
    pip install -r requirements.txt
    ```

5.  **Jalankan Aplikasi Streamlit:**
    * Pastikan Anda berada di direktori utama proyek.
    ```bash
    streamlit run app.py
    ```
    Aplikasi akan terbuka secara otomatis di *browser* Anda.

## Penulis

* **Nama:** Muhammad Ashim Izzuddin
* **Email:** muhammadashimizzuddin@gmail.com
* **Profil Dicoding:** https://www.dicoding.com/users/ashim_izzuddin/
