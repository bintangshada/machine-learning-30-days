Yoshhh, kita lanjut ke **Hari 5**! 🔥

---

# 📅 **Hari 5: Data Preprocessing untuk Machine Learning**

## 🎯 Tujuan Hari Ini:
Sebelum data bisa digunakan untuk membuat model ML, kita perlu melakukan **preprocessing**, yaitu:
- Membersihkan data
- Menangani data kosong (missing value)
- Menyiapkan data numerik/kategorikal
- Normalisasi/standardisasi
- Split data jadi train/test

---

## 📦 Tools yang Digunakan:
```python
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
```

---

## 📚 Materi Inti & Penjelasan

---

### ✅ 1. **Cek dan Tangani Missing Value**
```python
data.isnull().sum()   # Lihat jumlah missing value per kolom
data.dropna()         # Hapus baris yang punya nilai kosong
data.fillna(0)        # Isi nilai kosong dengan 0
```

---

### ✅ 2. **Pisahkan Fitur dan Target**
Misalnya kamu mau prediksi `Calories`, maka:
```python
X = data.drop('Calories', axis=1)  # Semua kolom kecuali Calories
y = data['Calories']               # Targetnya
```

---

### ✅ 3. **Split Data Train & Test**
Untuk melatih dan menguji model:
```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```

---

### ✅ 4. **Normalisasi / Standardisasi**
Skalakan data supaya semua fitur setara:
```python
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
```

---

## 🧪 Tugas Hari 5: Preprocessing Data `data.csv`

### ✅ Soal 1:
Cek apakah ada missing value di `data.csv`.  
Jika ada, isi dengan nilai rata-rata kolomnya.

---

### ✅ Soal 2:
Pisahkan fitur (`X`) dan target (`y`) — target: `Calories`.

---

### ✅ Soal 3:
Split data menjadi **train dan test** (80% : 20%).

---

### ✅ Soal 4:
Lakukan **standarisasi** pada fitur (X) menggunakan `StandardScaler`.

---

Kalau sudah dikerjakan, kirim file `.py` kamu dan aku akan review seperti biasa 😎  
Kalau mau aku buatin template awal, tinggal bilang ya!