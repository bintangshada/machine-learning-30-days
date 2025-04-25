# 📅 **Hari 6: Panduan Membangun Model ML dari Nol (Regresi)**

---

## 💡 Problem:
Kita ingin **memprediksi `Calories`** berdasarkan data seperti:
- Duration
- Pulse
- Maxpulse

---

## 🔢 Langkah-Langkah (Urutannya):

---

### 🧩 1. **Import Library Penting**
> Kamu butuh:
- `pandas` → untuk baca data
- `scikit-learn` (`sklearn`) → untuk model ML, preprocessing, evaluasi

---

### 📥 2. **Baca File CSV**
Gunakan `pandas.read_csv()` untuk load `data.csv`

---

### 🧽 3. **Tangani Missing Value**
Cek apakah ada nilai kosong. Kalau ada:
- Bisa hapus
- Bisa isi dengan rata-rata

---

### 🎯 4. **Pisahkan Fitur dan Target**
- Fitur = semua kolom kecuali `Calories`
- Target = `Calories`

---

### ✂️ 5. **Split Train dan Test**
Pakai `train_test_split` dari `sklearn.model_selection`

- Rasio umum: 80% training, 20% testing

---

### 📏 6. **Standarisasi Data**
Pakai `StandardScaler` untuk scaling fitur (`X_train` dan `X_test`)

---

### 🤖 7. **Latih Model Linear Regression**
- Gunakan `LinearRegression()` dari `sklearn.linear_model`
- `.fit(X_train_scaled, y_train)`

---

### 🔮 8. **Prediksi**
- Gunakan `.predict(X_test_scaled)` untuk memprediksi `Calories`

---

### 📊 9. **Evaluasi Model**
- Hitung `Mean Squared Error (MSE)`
- Hitung `R^2 Score`

---

## 🧪 Tugas Hari 6

Berdasarkan panduan di atas, kamu kerjakan hal berikut:

1. Load dan bersihkan data `data.csv`
2. Pisahkan fitur (`X`) dan target (`y`)
3. Split ke data latih dan uji
4. Standarisasi data fitur
5. Bangun model Linear Regression
6. Latih model dan lakukan prediksi
7. Evaluasi hasil dengan MSE dan R² Score

---

Kalau kamu mau, aku juga bisa kasih *expected output* biar kamu tahu kamu di jalur yang benar.  
Kalau udah selesai coding-nya, langsung kirim aja file `.py`-mu dan aku siap review 💯