import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Dashboard Performa Siswa", layout="wide")
df = pd.read_csv('data.csv', sep=';')  # Muat data asli
# Lakukan preprocessing sederhana yang diperlukan untuk visualisasi

st.title("Dashboard Monitoring Performa Siswa Jaya Jaya Institut")

# Sidebar untuk filter
st.sidebar.header("Filter Data:")
course = st.sidebar.selectbox("Pilih Program Studi:", options=df['Course'].unique())
filtered_df = df[df['Course'] == course]

# Tampilkan metrik utama
total_students = filtered_df.shape[0]
dropout_rate = (filtered_df[filtered_df['Status'] == 'Dropout'].shape[0] / total_students) * 100
st.metric("Total Mahasiswa di Prodi Ini", total_students)
st.metric("Tingkat Dropout", f"{dropout_rate:.2f}%")

# Visualisasi...
fig_status = px.bar(filtered_df['Status'].value_counts(), title="Distribusi Status Mahasiswa")
st.plotly_chart(fig_status)