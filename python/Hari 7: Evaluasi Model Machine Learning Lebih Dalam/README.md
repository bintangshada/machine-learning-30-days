# 📅 **Hari 7: Evaluasi Model Machine Learning Lebih Dalam**

---

## 🎯 Tujuan Hari Ini:
- Mengerti **kenapa** kita perlu evaluasi model lebih dari sekadar "training berhasil"
- Pakai **metrik evaluasi** untuk melihat kualitas prediksi
- Membandingkan model kalau mau

---

## 📦 Tools yang Dipakai:
```python
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import matplotlib.pyplot as plt
```

---

# 📚 Materi Inti dan Penjelasan

---

### ✅ 1. Kenapa Harus Evaluasi?
> Kalau cuma lihat hasil training, kita **bisa tertipu**: mungkin modelnya **overfitting** (bagus di data latih, jelek di data baru).  
Evaluasi itu kayak **ujian** buat tahu seberapa jago model di dunia nyata.

---

### ✅ 2. Metrik Evaluasi Regresi:

| Metrik | Artinya | Target |
|--------|---------|--------|
| **MAE** (Mean Absolute Error) | Rata-rata error absolut | Kecil |
| **MSE** (Mean Squared Error) | Rata-rata error kuadrat | Kecil |
| **R² Score** | Seberapa besar model menjelaskan variasi data | Mendekati 1 |

---

### ✅ 3. Hitung Evaluasi:
```python
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Mean Absolute Error:", mae)
print("Mean Squared Error:", mse)
print("R^2 Score:", r2)
```

---

### ✅ 4. Visualisasi Prediksi vs Kenyataan
> Kita juga bisa lihat **plot** antara nilai asli (`y_test`) dan nilai prediksi (`y_pred`)

```python
import matplotlib.pyplot as plt

plt.scatter(y_test, y_pred)
plt.xlabel("Actual Calories")
plt.ylabel("Predicted Calories")
plt.title("Actual vs Predicted Calories")
plt.show()
```
Kalau scatter plot mendekati garis lurus = model kamu bagus!

---

# 🧪 Tugas Hari 7:

1. Setelah kamu buat model di Hari 6,
2. Evaluasi model dengan:
   - MAE
   - MSE
   - R² Score
3. Buat scatter plot antara **Actual Calories** dan **Predicted Calories**

---

Kalau kamu sudah kerjakan Hari 5, 6, dan 7 nanti, kirim aja file `.py` kamu semua sekalian, aku review bareng ✨

Kalau mau sekalian nanti aku bantu kasih ide **pengembangan proyek dari data ini ke project mini ML**, tinggal bilang ya Shada! 🚀  
Gas terus?!