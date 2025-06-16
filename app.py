# app.py (Halaman Utama)

import streamlit as st

# Mengatur konfigurasi halaman
st.set_page_config(
    page_title="Analisis Dropout Mahasiswa",
    page_icon="🎓",
    layout="wide"
)

# Menulis judul dan deskripsi halaman utama
st.title('Analisis dan Prediksi Dropout Mahasiswa')

st.write(
    """
    Selamat datang di proyek analisis dan prediksi tingkat *dropout* mahasiswa di Jaya Jaya Institut.
    
    Proyek ini bertujuan untuk:
    1.  **Menganalisis** faktor-faktor kunci yang memengaruhi status kelulusan mahasiswa.
    2.  **Membangun model Machine Learning** untuk memprediksi mahasiswa yang berpotensi *dropout*.
    
    Silakan gunakan menu navigasi di sebelah kiri untuk berpindah ke halaman **Analisis Data** atau **Prediksi Mahasiswa**.
    """
)

st.info("Pilih halaman dari sidebar untuk memulai.")