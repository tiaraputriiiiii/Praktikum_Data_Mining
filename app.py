import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

# Data WHO
who_data = {
    12: {'tb_median': 75, 'tb_sd': 3},
    24: {'tb_median': 85, 'tb_sd': 3.5},
    36: {'tb_median': 95, 'tb_sd': 4},
    48: {'tb_median': 100, 'tb_sd': 4.5},
    60: {'tb_median': 105, 'tb_sd': 5}
}

# Styling
st.markdown("""
<style>
body, .css-18e3th9 {background: linear-gradient(135deg, #f0f4ff, #d9e2ff); font-family: 'Segoe UI';}
h1, h3 {text-align: center; color: #003366;}
.stButton > button {
    background-color: #0059b3 !important; color: white !important; font-weight: bold !important;
}
.result-box {background: #e6f0ff; padding: 25px; border-radius: 10px; text-align: center;}
.result-stunting {color: #b30000; font-weight: bold;}
.result-normal {color: #004080; font-weight: bold;}
</style>
""", unsafe_allow_html=True)

st.title("Prediksi Stunting Anak")

# Upload CSV
uploaded_file = st.file_uploader("Upload Dataset CSV", type="csv")

if uploaded_file is not None:
    try:
        data = pd.read_csv(uploaded_file)
        st.success("✅ Dataset berhasil dimuat.")
    except Exception as e:
        st.error(f"❌ Gagal membaca file: {e}")
        st.stop()
else:
    st.info("📂 Menggunakan data default karena belum ada file diupload.")
    data = pd.DataFrame({
        'umur': [12, 24, 36, 48, 60, 12, 24, 36, 48, 60],
        'jenis_kelamin': [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
        'berat': [7, 8.5, 10, 11, 12, 5.5, 7, 8, 9, 10],
        'tinggi': [70, 80, 90, 95, 100, 60, 70, 80, 85, 90],
        'lingkar_lengan': [12, 13, 14, 15, 16, 11, 12, 12, 13, 14],
        'lingkar_kepala': [44, 46, 48, 49, 50, 42, 43, 45, 46, 47],
        'stunting': [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
    })

# Model Decision Tree
fitur = ['umur', 'jenis_kelamin', 'berat', 'tinggi', 'lingkar_lengan', 'lingkar_kepala']
X = data[fitur]
y = data['stunting']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = DecisionTreeClassifier(max_depth=3, random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
akurasi = accuracy_score(y_test, y_pred)

st.markdown("<h3>Masukkan Data Anak</h3>", unsafe_allow_html=True)
# Input data manual
col1, col2 = st.columns(2)
with col1:
    jenis_kelamin_str = st.selectbox("Jenis Kelamin", ["Laki-laki", "Perempuan"])
    jenis_kelamin = 1 if jenis_kelamin_str == "Laki-laki" else 0
    umur = st.number_input("Umur (bulan)", 0, 60, 12)
    berat = st.number_input("Berat badan (kg)", 1.0, 30.0, 9.0)

with col2:
    tinggi = st.number_input("Tinggi badan (cm)", 30.0, 150.0, 75.0)
    lingkar_kepala = st.number_input("Lingkar kepala (cm)", 30.0, 60.0, 45.0)
    lingkar_lengan = st.number_input("Lingkar lengan (cm)", 10.0, 30.0, 15.0)

if st.button("Prediksi"):
    usia_terdekat = min(who_data.keys(), key=lambda x: abs(x - umur))
    who = who_data[usia_terdekat]
    z_tb = (tinggi - who['tb_median']) / who['tb_sd']

    if z_tb < -3:
        status_who = "Sangat Pendek (Stunting Berat)"
    elif z_tb < -2:
        status_who = "Pendek (Stunting Ringan)"
    else:
        status_who = "Normal"

    pred = model.predict([[umur, jenis_kelamin, berat, tinggi, lingkar_lengan, lingkar_kepala]])[0]
    label = "Stunting" if pred == 1 else "Tidak Stunting"

    st.markdown(f"""
    <div class="result-box">
        <div class="{ 'result-stunting' if pred == 1 else 'result-normal' }">
            Hasil Prediksi: <strong>{label}</strong><br/>
            Status WHO: <strong>{status_who}</strong>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Grafik Hasil Prediksi Decision Tree
   # Visualisasi hasil klasifikasi dengan scatter plot
    st.markdown("<h3>Visualisasi Hasil Prediksi Model (Scatter Plot)</h3>", unsafe_allow_html=True)

    # Gunakan dua fitur utama untuk visualisasi: berat dan tinggi
    X_vis = X_test.copy()
    X_vis['prediksi'] = y_pred

    fig, ax = plt.subplots()
    colors = {0: '#004080', 1: '#b30000'}

    for kelas in X_vis['prediksi'].unique():
        subset = X_vis[X_vis['prediksi'] == kelas]
        ax.scatter(subset['tinggi'], subset['berat'],
                label='Tidak Stunting' if kelas == 0 else 'Stunting',
                c=colors[kelas], s=80, alpha=0.7, edgecolors='k')

    # Titik anak yang diprediksi manual
    ax.scatter(tinggi, berat, label='Anak Anda', c='purple', s=120, marker='X', edgecolors='black')

    ax.set_xlabel("Tinggi Badan (cm)")
    ax.set_ylabel("Berat Badan (kg)")
    ax.set_title("Hasil Prediksi Model Decision Tree")
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)


    if pred == 1 or status_who != "Normal":
        st.warning("⚠️ Anak berpotensi mengalami stunting. Disarankan konsultasi ke tenaga medis.")
    else:
        st.success("✅ Pertumbuhan anak dalam kategori normal. Terus jaga asupan gizi dan pantau perkembangan.")
