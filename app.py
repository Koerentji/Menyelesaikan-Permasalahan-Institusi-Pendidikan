import streamlit as st
import pandas as pd
import pickle
import numpy as np

# Memuat model dan scaler
with open('model/xgb_model.pkl', 'rb') as f:
    model = pickle.load(f)
with open('model/scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

st.title("Prediksi Potensi Dropout Mahasiswa")

# Membuat form untuk input
with st.form("prediction_form"):
    st.header("Masukkan Data Mahasiswa:")
    # Buat input fields sesuai selected_features di notebook
    tuition_fees = st.selectbox("Status UKT Lunas?", [1, 0], format_func=lambda x: 'Ya' if x == 1 else 'Tidak')
    scholarship = st.selectbox("Penerima Beasiswa?", [1, 0], format_func=lambda x: 'Ya' if x == 1 else 'Tidak')
    age = st.number_input("Usia Saat Mendaftar", 17, 70, 20)
    # ... tambahkan input lain ...
    gdp = st.slider("GDP", -4.0, 4.0, 0.0)

    # Tombol submit
    submitted = st.form_submit_button("Prediksi")

    if submitted:
        # Proses input dan lakukan prediksi
        input_data = np.array([[tuition_fees, scholarship, age, gdp]])  # sesuaikan urutan dengan selected_features
        input_data_scaled = scaler.transform(input_data)
        prediction = model.predict(input_data_scaled)
        prediction_proba = model.predict_proba(input_data_scaled)

        st.subheader("Hasil Prediksi:")
        if prediction[0] == 1:
            st.error(f"Mahasiswa Berpotensi Dropout (Probabilitas: {prediction_proba[0][1]*100:.2f}%)")
            st.warning("Direkomendasikan untuk memberikan bimbingan khusus.")
        else:
            st.success(f"Mahasiswa Berpotensi Lulus (Probabilitas Dropout: {prediction_proba[0][1]*100:.2f}%)")