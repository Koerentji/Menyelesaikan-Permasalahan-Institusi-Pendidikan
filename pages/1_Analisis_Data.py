# pages/1_Analisis_Data.py

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title('📊 Analisis Data Mahasiswa')

# Fungsi untuk memuat data (menggunakan cache agar efisien)
@st.cache_data
def load_data():
    try:
        data = pd.read_csv('data.csv', sep=';')
        return data
    except FileNotFoundError:
        st.error("File 'data.csv' tidak ditemukan. Pastikan file berada di direktori utama.")
        return None

df = load_data()

if df is not None:
    st.write("Berikut adalah beberapa visualisasi kunci dari data mahasiswa Jaya Jaya Institut.")

    # --- Visualisasi 1: Distribusi Status Mahasiswa ---
    st.subheader('1. Distribusi Status Kelulusan Mahasiswa')
    fig1, ax1 = plt.subplots(figsize=(8, 5))
    sns.countplot(x='Status', data=df, ax=ax1, palette='viridis')
    ax1.set_title('Distribusi Status Mahasiswa')
    ax1.set_xlabel('Status')
    ax1.set_ylabel('Jumlah Mahasiswa')
    st.pyplot(fig1)
    
    st.markdown(
        """
        **Insight:**
        - **Graduate (Lulus):** Merupakan kelompok terbesar, menunjukkan mayoritas mahasiswa berhasil menyelesaikan studi.
        - **Dropout:** Kelompok ini memiliki jumlah yang sangat signifikan, yang menjadi fokus utama masalah institusi.
        - **Enrolled (Terdaftar):** Merupakan mahasiswa yang masih aktif.
        """
    )
    st.markdown("---")


    # --- Visualisasi 2: Hubungan dengan Beasiswa ---
    st.subheader('2. Hubungan Status dengan Kepemilikan Beasiswa')
    fig2, ax2 = plt.subplots(figsize=(10, 6))
    sns.countplot(x='Scholarship_holder', hue='Status', data=df, ax=ax2, palette='magma')
    ax2.set_title('Hubungan Status Mahasiswa dengan Kepemilikan Beasiswa')
    ax2.set_xlabel('Status Beasiswa')
    ax2.set_ylabel('Jumlah Mahasiswa')
    ax2.set_xticklabels(['Tidak Punya Beasiswa', 'Punya Beasiswa'])
    st.pyplot(fig2)

    st.markdown(
        """
        **Insight:**
        - Proporsi mahasiswa **Dropout** secara signifikan **lebih rendah** pada kelompok yang memiliki beasiswa.
        - Sebaliknya, proporsi mahasiswa **Graduate** jauh **lebih tinggi** pada kelompok penerima beasiswa.
        - Ini mengindikasikan bahwa beasiswa adalah faktor protektif yang kuat terhadap risiko *dropout*.
        """
    )
    st.markdown("---")


    # --- Visualisasi 3: Hubungan dengan Usia ---
    st.subheader('3. Distribusi Usia Berdasarkan Status')
    fig3, ax3 = plt.subplots(figsize=(12, 7))
    sns.boxplot(x='Status', y='Age_at_enrollment', data=df, ax=ax3, palette='coolwarm')
    ax3.set_title('Distribusi Usia Saat Mendaftar Berdasarkan Status Mahasiswa')
    ax3.set_xlabel('Status')
    ax3.set_ylabel('Usia Saat Mendaftar')
    st.pyplot(fig3)

    st.markdown(
        """
        **Insight:**
        - Mahasiswa yang **Lulus** cenderung mendaftar pada usia yang lebih muda.
        - Kelompok **Dropout** memiliki rentang usia yang paling lebar dan median usia yang paling tinggi.
        - Ini menunjukkan bahwa mahasiswa yang lebih tua (*mature students*) memiliki risiko *dropout* yang lebih tinggi.
        """
    )