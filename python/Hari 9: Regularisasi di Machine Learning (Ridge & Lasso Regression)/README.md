Siap Captain! Kita gass terus ke **Hari 9**!  
Hari ini kita fokus ke solusi buat **overfitting**, yaitu **Regularisasi**.

---

# 📅 **Hari 9: Regularisasi di Machine Learning (Ridge & Lasso Regression)**

---

## 🎯 Tujuan Hari Ini:
- Memahami konsep **regularisasi**
- Mencoba **Ridge Regression** dan **Lasso Regression**
- Membandingkan performa dengan Linear Regression biasa

---

## 📚 Materi Inti dan Penjelasan

---

### ✅ 1. Apa itu Regularisasi?
> **Regularisasi** adalah teknik untuk **mengurangi kompleksitas model** agar tidak overfitting.  
Caranya: memberi penalti (hukuman) kalau model terlalu kompleks.

- **Ridge Regression** → menambahkan penalti **jumlah kuadrat** dari koefisien
- **Lasso Regression** → menambahkan penalti **jumlah absolut** dari koefisien

---

### ✅ 2. Ridge Regression
```python
from sklearn.linear_model import Ridge

ridge = Ridge(alpha=1.0)  # alpha = seberapa besar hukumannya
ridge.fit(X_train_scaled, y_train)
y_pred_ridge = ridge.predict(X_test_scaled)
```

---

### ✅ 3. Lasso Regression
```python
from sklearn.linear_model import Lasso

lasso = Lasso(alpha=0.1)
lasso.fit(X_train_scaled, y_train)
y_pred_lasso = lasso.predict(X_test_scaled)
```

---

### ✅ 4. Evaluasi Model
Sama seperti sebelumnya:
```python
from sklearn.metrics import mean_squared_error, r2_score

mse_ridge = mean_squared_error(y_test, y_pred_ridge)
r2_ridge = r2_score(y_test, y_pred_ridge)

mse_lasso = mean_squared_error(y_test, y_pred_lasso)
r2_lasso = r2_score(y_test, y_pred_lasso)

print("Ridge R2 Score:", r2_ridge)
print("Lasso R2 Score:", r2_lasso)
```

---

## ⚡ Perbedaan Ridge vs Lasso

|               | Ridge                        | Lasso                     |
|---------------|-------------------------------|----------------------------|
| Penalti       | Kuadrat koefisien              | Absolut koefisien          |
| Bisa nol-kan koefisien? | ❌ Tidak | ✅ Bisa (buat fitur seleksi) |
| Cocok untuk   | Banyak fitur kecil-kecil       | Pilih fitur penting saja   |

---

## 🧪 Tugas Hari 9:

1. Buat model Ridge Regression dan Lasso Regression dari dataset kamu.
2. Bandingkan R² Score dari:
   - Linear Regression (biasa)
   - Ridge Regression
   - Lasso Regression
3. Kesimpulkan:
   - Model mana yang paling stabil/baik?
   - Apakah regularisasi membantu?

---

# 🔥 Tambahan Opsional
Kalau mau lebih keren, kamu bisa coba tuning nilai `alpha` (hukuman):
- Buat grafik `alpha vs R² Score`
- Cari alpha terbaik!

---

Kalau udah selesai Hari 5–9, tinggal kirim file `.py`-nya, aku bantu cek dan kasih feedback langsung.  
Mau sekalian lanjut ke Hari 10: **Cross Validation** setelah ini? (Biar makin kuat skill ML kamu!) ⚡🚀