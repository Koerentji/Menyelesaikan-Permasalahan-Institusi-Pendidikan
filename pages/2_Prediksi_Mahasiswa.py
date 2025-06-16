# Mengimpor library yang diperlukan
import streamlit as st
import pandas as pd
import joblib
import os

# --- FUNGSI UNTUK MEMUAT MODEL ---
# Komentar: Menggunakan @st.cache_resource agar model, scaler, dan encoder hanya dimuat sekali
@st.cache_resource
def load_artifacts():
    """
    Fungsi ini memuat model, scaler, dan label encoder yang telah disimpan.
    Menggunakan cache Streamlit untuk efisiensi.
    """
    try:
        model = joblib.load('model/model_rf.pkl')
        scaler = joblib.load('model/scaler.pkl')
        label_encoder = joblib.load('model/label_encoder.pkl')
        return model, scaler, label_encoder
    except FileNotFoundError:
        st.error("File model tidak ditemukan. Pastikan file 'model_rf.pkl', 'scaler.pkl', dan 'label_encoder.pkl' ada di dalam folder 'model/'.")
        return None, None, None
    except Exception as e:
        st.error(f"Terjadi error saat memuat model: {e}")
        return None, None, None

# --- MEMUAT ARTIFAK ---
model, scaler, label_encoder = load_artifacts()

# --- JUDUL DAN DESKRIPSI APLIKASI ---
st.title('🎓 Prediksi Status Kelulusan Mahasiswa')
st.write(
    """
    Selamat datang di aplikasi prediksi status kelulusan mahasiswa Jaya Jaya Institut.
    Aplikasi ini menggunakan model Machine Learning untuk memprediksi apakah seorang mahasiswa 
    akan **Lulus**, **Dropout**, atau **Masih Terdaftar**.
    """
)
st.write("Silakan masukkan data mahasiswa di **sidebar kiri** untuk memulai.")

# --- SIDEBAR UNTUK INPUT PENGGUNA ---
st.sidebar.header('Masukkan Data Mahasiswa:')

# Komentar: Membuat fungsi untuk menampung semua input dari sidebar.
def user_input_features():
    """
    Fungsi ini membuat widget input di sidebar Streamlit untuk mengumpulkan
    data dari pengguna dan mengembalikannya sebagai DataFrame.
    """
    # --- Input berdasarkan fitur terpenting ---
    st.sidebar.subheader('⭐ Fitur Akademik Utama')
    
    # Nilai dan SKS lulus adalah fitur paling penting, jadi kita letakkan di atas.
    curricular_units_2nd_sem_approved = st.sidebar.slider('Jumlah SKS Lulus (Semester 2)', 0, 25, 10)
    curricular_units_2nd_sem_grade = st.sidebar.slider('Nilai Rata-rata (Semester 2)', 0.0, 20.0, 12.0)
    curricular_units_1st_sem_approved = st.sidebar.slider('Jumlah SKS Lulus (Semester 1)', 0, 25, 9)
    curricular_units_1st_sem_grade = st.sidebar.slider('Nilai Rata-rata (Semester 1)', 0.0, 20.0, 12.0)
    
    tuition_fees_up_to_date = st.sidebar.selectbox('Status Pembayaran SPP', ('Lancar', 'Menunggak'))
    
    st.sidebar.subheader('👤 Fitur Demografis & Lainnya')
    age_at_enrollment = st.sidebar.slider('Usia Saat Mendaftar', 17, 70, 20)
    scholarship_holder = st.sidebar.selectbox('Penerima Beasiswa', ('Ya', 'Tidak'))
    debtor = st.sidebar.selectbox('Memiliki Hutang', ('Ya', 'Tidak'))
    gender = st.sidebar.selectbox('Jenis Kelamin', ('Laki-laki', 'Perempuan'))
    
    # --- Membuat DataFrame dari input ---
    # Komentar: Kita perlu mengubah input pengguna menjadi format yang sama dengan data latih
    # termasuk mengubah 'Ya'/'Tidak' menjadi 1/0.
    
    # Mapping dari input pengguna ke nilai numerik
    tuition_map = {'Lancar': 1, 'Menunggak': 0}
    scholarship_map = {'Ya': 1, 'Tidak': 0}
    debtor_map = {'Ya': 1, 'Tidak': 0}
    gender_map = {'Laki-laki': 1, 'Perempuan': 0}
    
    # Membuat dictionary untuk semua fitur.
    # PENTING: Nama kolom harus SAMA PERSIS dengan saat melatih model.
    data = {
        'Marital_status': 1, # Default value
        'Application_mode': 1, # Default value
        'Application_order': 1, # Default value
        'Course': 9119, # Default value (misal: salah satu course)
        'Daytime_evening_attendance': 1, # Default value
        'Previous_qualification': 1, # Default value
        'Previous_qualification_grade': 130.0, # Default value
        'Nacionality': 1, # Default value
        'Mothers_qualification': 1, # Default value
        'Fathers_qualification': 1, # Default value
        'Mothers_occupation': 5, # Default value
        'Fathers_occupation': 5, # Default value
        'Admission_grade': 125.0, # Default value
        'Displaced': 0, # Default value
        'Educational_special_needs': 0, # Default value
        'Debtor': debtor_map[debtor],
        'Tuition_fees_up_to_date': tuition_map[tuition_fees_up_to_date],
        'Gender': gender_map[gender],
        'Scholarship_holder': scholarship_map[scholarship_holder],
        'Age_at_enrollment': age_at_enrollment,
        'International': 0, # Default value
        'Curricular_units_1st_sem_credited': 0, # Default value
        'Curricular_units_1st_sem_enrolled': 10, # Default value
        'Curricular_units_1st_sem_evaluations': 10, # Default value
        'Curricular_units_1st_sem_approved': curricular_units_1st_sem_approved,
        'Curricular_units_1st_sem_grade': curricular_units_1st_sem_grade,
        'Curricular_units_1st_sem_without_evaluations': 0, # Default value
        'Curricular_units_2nd_sem_credited': 0, # Default value
        'Curricular_units_2nd_sem_enrolled': 10, # Default value
        'Curricular_units_2nd_sem_evaluations': 10, # Default value
        'Curricular_units_2nd_sem_approved': curricular_units_2nd_sem_approved,
        'Curricular_units_2nd_sem_grade': curricular_units_2nd_sem_grade,
        'Curricular_units_2nd_sem_without_evaluations': 0, # Default value
        'Unemployment_rate': 12.0, # Default value
        'Inflation_rate': 1.0, # Default value
        'GDP': 0.0, # Default value
    }
    
    # Mengubah dictionary menjadi DataFrame
    features = pd.DataFrame(data, index=[0])
    return features

# --- JIKA MODEL BERHASIL DIMUAT, TAMPILKAN APLIKASI ---
if model and scaler and label_encoder:
    # Memanggil fungsi untuk mendapatkan input dari pengguna
    input_df = user_input_features()

    # Menampilkan data yang dimasukkan pengguna
    st.subheader('Data Mahasiswa yang Dimasukkan:')
    st.write(input_df)

    # Membuat tombol untuk prediksi
    if st.sidebar.button('**Prediksi Sekarang!**'):
        # 1. Scaling data input
        input_scaled = scaler.transform(input_df)
        
        # 2. Melakukan prediksi
        prediction = model.predict(input_scaled)
        prediction_proba = model.predict_proba(input_scaled)
        
        # 3. Mengubah hasil prediksi numerik kembali ke label asli
        prediction_label = label_encoder.inverse_transform(prediction)[0]
        
        # Menampilkan hasil prediksi
        st.subheader('Hasil Prediksi Status Mahasiswa:')
        
        # Mengatur warna dan ikon berdasarkan hasil
        if prediction_label == 'Dropout':
            st.error(f'**{prediction_label}** 😥', icon="🚨")
        elif prediction_label == 'Graduate':
            st.success(f'**{prediction_label}** 🎉', icon="🎓")
        else: # Enrolled
            st.info(f'**{prediction_label}** 🤔', icon="📚")
            
        # Menampilkan probabilitas
        st.write("Probabilitas Hasil:")
        proba_df = pd.DataFrame(prediction_proba, columns=label_encoder.classes_)
        st.write(proba_df)

else:
    st.warning("Aplikasi tidak dapat berjalan karena model tidak berhasil dimuat.")