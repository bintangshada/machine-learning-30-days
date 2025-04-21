Let's gooo! 🚀 Hari ke-2 kita masuk ke library penting dalam Machine Learning, yaitu:

# 📅 **Hari 2: NumPy – Dasar Manipulasi Data Numerik**

---

## 🎯 Tujuan Hari Ini
- Memahami konsep array di NumPy
- Melakukan operasi numerik dasar
- Mempersiapkan fondasi untuk data preprocessing di ML

---

## 📦 Apa itu NumPy?

**NumPy** (Numerical Python) adalah library Python untuk:
- Operasi matematika cepat
- Manipulasi array multidimensi
- Basis utama dari banyak library ML (kayak Pandas, TensorFlow, dll)

---

## 📚 Materi Inti

### ✅ 1. Instal dan Import NumPy
```python
import numpy as np
```

### ✅ 2. Membuat Array
```python
a = np.array([1, 2, 3])             # 1D array
b = np.array([[1, 2], [3, 4]])      # 2D array
print(a)
print(b)
```

### ✅ 3. Ukuran dan Dimensi
```python
print(a.shape)     # (3,)
print(b.shape)     # (2, 2)
print(a.ndim)      # 1
print(b.ndim)      # 2
```

### ✅ 4. Operasi Aritmatika
```python
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
print(x + y)        # Penjumlahan
print(x * y)        # Perkalian elemen
print(x.dot(y))     # Perkalian dot product
```

### ✅ 5. Fungsi Statistik
```python
arr = np.array([1, 2, 3, 4])
print(np.mean(arr))    # Rata-rata
print(np.std(arr))     # Standar deviasi
print(np.max(arr))     # Nilai maksimum
print(np.min(arr))     # Nilai minimum
```

---

## 🧪 Tugas Praktik Hari 2

### 🧠 Latihan 1:
Buat array NumPy `a = [10, 20, 30, 40, 50]`. Hitung:
- Rata-rata
- Maksimum
- Minimum
- Standar deviasi

### 🧠 Latihan 2:
Buat dua array `x = [1, 2, 3]` dan `y = [4, 5, 6]`. Hitung:
- Penjumlahan
- Perkalian elemen
- Dot product

### 🧠 Latihan 3:
Buat array 2D `matrix = [[1, 2], [3, 4]]`. Cetak:
- Jumlah elemen
- Dimensi array
- Bentuk array

---

Kalau kamu sudah selesai, upload lagi filenya dan aku akan periksa langsung. Kita gass terus sampai bisa ML kayak pro! 💻🔥