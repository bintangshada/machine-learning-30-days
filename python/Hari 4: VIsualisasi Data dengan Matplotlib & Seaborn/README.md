**Hari 4: Visualisasi Data** dengan penjelasan yang **lebih mendalam dan pelan-pelan** biar makin paham, terutama untuk kamu yang baru belajar 📊✨

---

# 📅 **Hari 4: Visualisasi Data dengan Matplotlib & Seaborn**

## 🎯 Tujuan:
- Belajar menggambar grafik dengan Python
- Memahami jenis-jenis grafik: **line chart**, **bar chart**, **histogram**, **scatter plot**
- Melatih kemampuan membaca pola dari grafik

---

## 📦 Tools yang Dipakai

### 1. **Matplotlib**
- Library grafik paling dasar
- Cocok untuk kontrol penuh (bentuk, warna, dll)

### 2. **Seaborn**
- Dibangun di atas Matplotlib
- Grafik lebih **cantik** dan siap pakai
- Terintegrasi bagus dengan DataFrame (Pandas)

---

## 📚 Materi Inti dan Penjelasannya

---

### ✅ **1. Line Plot (Garis)**
> Cocok untuk data yang punya urutan waktu atau urutan naik turun (trend)

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

plt.plot(x, y)  # gambar garis dari titik-titik x dan y
plt.title("Contoh Line Plot")
plt.xlabel("X")  # label sumbu x
plt.ylabel("Y")  # label sumbu y
plt.show()       # tampilkan grafik
```

---

### ✅ **2. Bar Chart (Batang)**
> Cocok untuk data kategori, seperti jumlah siswa per jurusan

```python
kategori = ['A', 'B', 'C']
nilai = [10, 20, 15]

plt.bar(kategori, nilai)
plt.title("Contoh Bar Chart")
plt.show()
```

---

### ✅ **3. Histogram**
> Digunakan untuk melihat **distribusi data** (berapa banyak nilai yang muncul di rentang tertentu)

```python
import numpy as np

data = np.random.randn(100)  # 100 angka acak (distribusi normal)
plt.hist(data, bins=10)      # "bins" adalah jumlah kelompok
plt.title("Contoh Histogram")
plt.show()
```

---

### ✅ **4. Scatter Plot (Titik-Titik)**
> Bagus untuk lihat **hubungan** antara dua variabel numerik (apakah saling memengaruhi?)

```python
x = [5, 7, 8, 7, 2]
y = [99, 86, 87, 88, 100]

plt.scatter(x, y)
plt.title("Contoh Scatter Plot")
plt.show()
```

---

### ✅ **5. Seaborn (Versi Lebih Cantik & Mudah)**
```python
import seaborn as sns

# Load contoh data dari Seaborn
tips = sns.load_dataset('tips')

# Scatter plot antara total tagihan dan tip
sns.scatterplot(data=tips, x='total_bill', y='tip')
plt.title("Scatterplot Total Bill vs Tip")
plt.show()
```

---

## 🧪 **Tugas Hari 4: Visualisasi**

### Soal 1: Line Plot
Buat line chart dari:
- x = [1, 2, 3, 4, 5]
- y = [10, 12, 15, 20, 30]

---

### Soal 2: Bar Chart
Kategori: ["A", "B", "C", "D"]  
Nilai: [5, 10, 15, 7]

---

### Soal 3: Histogram
Buat histogram dari:
- 100 angka acak: `np.random.randn(100)`
- Gunakan `bins=15`

---

### Soal 4: Scatter Plot
x = [1,2,3,4,5]  
y = [5,4,3,2,1]

---

### 💥 Soal Bonus:
Ambil kolom **Calories** dari file `data.csv` milikmu, lalu buat **histogram** untuk menampilkan sebaran kalorinya.

---

Kalau udah kamu kerjain, upload lagi filenya dan aku siap bantu review!  
Kalau masih bingung dengan satu jenis grafik, tinggal bilang — aku siap bantuin bikin contoh visual juga! 😎