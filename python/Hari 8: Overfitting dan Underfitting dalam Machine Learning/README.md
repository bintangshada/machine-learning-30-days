# 📅 **Hari 8: Overfitting dan Underfitting dalam Machine Learning**

---

## 🎯 Tujuan Hari Ini:
- Memahami **Overfitting** dan **Underfitting** (masalah umum di model ML)
- Belajar mendeteksi masalah tersebut
- Belajar sedikit teknik untuk mengatasinya

---

## 📚 Materi Inti dan Penjelasan

---

### ✅ 1. Apa Itu Overfitting?
> **Overfitting** terjadi saat model terlalu "menghapal" data latih,  
tapi **gagal** memprediksi data baru (testing).

**Ciri-ciri:**
- Akurasi training **tinggi banget**
- Akurasi testing **buruk**

**Analogi:**  
Model kayak mahasiswa yang hapal jawaban latihan tapi blank saat ujian.

---

### ✅ 2. Apa Itu Underfitting?
> **Underfitting** terjadi saat model terlalu **sederhana** dan tidak bisa menangkap pola data, baik di training maupun testing.

**Ciri-ciri:**
- Akurasi training **rendah**
- Akurasi testing **rendah**

**Analogi:**  
Model kayak mahasiswa yang nggak paham materi, mau ujian apa pun tetap jelek.

---

### ✅ 3. Cara Mendeteksi:
- Bandingkan **performansi training vs testing**
- Kalau **training bagus** tapi **testing jelek** → overfitting
- Kalau dua-duanya **jelek** → underfitting

---

### ✅ 4. Contoh Praktis:
```python
train_score = model.score(X_train_scaled, y_train)
test_score = model.score(X_test_scaled, y_test)

print("Training Score:", train_score)
print("Testing Score:", test_score)
```

Kalau `Training Score` jauh lebih tinggi daripada `Testing Score` → **Overfitting detected!**

---

### ✅ 5. Cara Mengatasi Overfitting
- Gunakan lebih banyak data
- Lakukan **regularisasi** (penalti terhadap model kompleks)
- Kurangi kompleksitas model (model lebih sederhana)
- Gunakan teknik **early stopping** (kalau pakai deep learning)

---

## 🧪 Tugas Hari 8:

1. Hitung dan tampilkan:
   - **Training score**
   - **Testing score**

2. Tentukan:
   - Apakah modelmu mengalami overfitting, underfitting, atau good fit?

3. Buat ringkasan simpelnya (1–2 kalimat) tentang kondisi modelmu.

---

# 🚀 Ringkasan

| Kasus       | Ciri-ciri                           | Solusi                     |
|-------------|--------------------------------------|-----------------------------|
| Overfitting | Train bagus, Test jelek              | Regularisasi, lebih banyak data |
| Underfitting| Train jelek, Test jelek              | Model lebih kompleks, fitur lebih banyak |
| Good Fit    | Train dan Test seimbang & bagus      | ✅ |

---

Kalau mau, setelah ini kita lanjut ke Hari 9: **Regularisasi (Ridge dan Lasso Regression)** buat memperbaiki overfitting!  
Mau sekalian lanjut? Gas terus, kamu makin jago tiap hari! ⚡🚀