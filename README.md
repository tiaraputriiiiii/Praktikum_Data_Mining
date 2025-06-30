# 📊 Aplikasi Prediksi Stunting Anak
Menggunakan Algoritma Decision Tree Berbasis Web dengan Streamlit

# 📝 Deskripsi Proyek

Aplikasi ini bertujuan untuk memprediksi risiko stunting pada anak-anak berdasarkan data fisik seperti umur, berat badan, dan tinggi badan. Aplikasi ini dibangun menggunakan framework Streamlit dan mengimplementasikan algoritma Decision Tree untuk klasifikasi status stunting.

# 🚀 Fitur Utama

- Upload dataset CSV
- Prediksi status stunting berdasarkan data masukan
- Pelatihan model Decision Tree secara langsung
- Evaluasi dan visualisasi akurasi model
- Antarmuka web interaktif berbasis Streamlit

# 📂 Struktur Proyek

```
PrediksiStunting/
├── app.py                  # Aplikasi utama Streamlit
├── dataset_stunting.csv    # Dataset stunting (contoh data)
├── requirements.txt
```

# ⚙️ Teknologi yang Digunakan

- Python 3.x
- Streamlit
- Scikit-learn
- Pandas
- Numpy
- Matplotlib

# 🔧 Cara Menjalankan Aplikasi
1. Clone repository ini

```
git clone https://github.com/username/PrediksiStunting.git
cd PrediksiStunting
```

2. Install semua dependensi
```
pip install streamlit scikit-learn pandas numpy matplotlib
```

3. Jalankan aplikasi
```
streamlit run app.py
```

# 📈 Tentang Dataset
Dataset yang digunakan (dataset_stunting.csv) berisi informasi berikut:

- Umur (dalam bulan)
- Berat badan (kg)
- Tinggi badan (cm)
- Lingkar lengan (cm)
- Lingkar kepala (cm)
- Status stunting (target klasifikasi: stunting / tidak)

# 🧠 Algoritma yang Digunakan
Model klasifikasi menggunakan Decision Tree Classifier dari pustaka scikit-learn. Algoritma ini cocok untuk klasifikasi berbasis aturan dan sangat mudah divisualisasikan.

# 📷 Screenshot

![Screenshot 2025-06-23 112131](https://github.com/user-attachments/assets/b2357c20-8c3d-4124-8f65-ceac8dec0474)

![Screenshot 2025-06-23 112201](https://github.com/user-attachments/assets/e5bf0517-eb33-4fa6-af55-0aa8eb27e78d)
