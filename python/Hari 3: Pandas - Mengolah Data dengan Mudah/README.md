Siap! Let's go, kita lanjut ke **Hari 3**: **Pandas**! 📊✨

---

# 📅 **Hari 3: Pandas – Mengolah Data dengan Mudah**

---

## 🎯 Tujuan Hari Ini
- Mengenal dan memahami **DataFrame** di Pandas
- Melakukan manipulasi data seperti **filtering**, **sorting**, dan **grouping**
- Mempersiapkan data untuk analisis lebih lanjut

---

## 📦 Apa itu Pandas?

**Pandas** adalah library Python untuk:
- Mengolah data tabular (seperti spreadsheet atau database)
- Memudahkan manipulasi data dengan **DataFrame** (struktur data utama Pandas)

---

## 📚 Materi Inti

### ✅ 1. Instal dan Import Pandas
```python
import pandas as pd
```

### ✅ 2. Membuat DataFrame dari Dictionary
```python
data = {'Nama': ['Alice', 'Bob', 'Charlie'],
        'Usia': [25, 30, 35],
        'Kota': ['New York', 'Los Angeles', 'Chicago']}

df = pd.DataFrame(data)
print(df)
```

### ✅ 3. Membaca Data dari CSV
```python
# Misalnya ada file 'data.csv'
df = pd.read_csv('data.csv')
print(df.head())  # Tampilkan 5 baris pertama
```

### ✅ 4. Memilih Kolom dan Baris
```python
print(df['Nama'])         # Pilih kolom 'Nama'
print(df[['Nama', 'Usia']])  # Pilih beberapa kolom

# Mengakses baris tertentu
print(df.iloc[0])         # Baris pertama
print(df.loc[0])          # Baris pertama (akses berdasarkan index label)
```

### ✅ 5. Filtering Data
```python
# Filter data berdasarkan kondisi
df_filtered = df[df['Usia'] > 30]
print(df_filtered)
```

### ✅ 6. Sorting Data
```python
df_sorted = df.sort_values(by='Usia', ascending=False)
print(df_sorted)
```

### ✅ 7. Grouping Data
```python
data = {'Kategori': ['A', 'B', 'A', 'B'],
        'Nilai': [10, 20, 30, 40]}
df = pd.DataFrame(data)

# Grouping dan menghitung rata-rata
df_grouped = df.groupby('Kategori')['Nilai'].mean()
print(df_grouped)
```

---

## 🧪 Tugas Praktik Hari 3

### 🧠 Latihan 1:
Buat DataFrame dengan data berikut:
- Kolom `Nama`: ["Andi", "Budi", "Citra"]
- Kolom `Usia`: [22, 25, 28]
- Kolom `Pekerjaan`: ["Programmer", "Designer", "Manager"]

Lakukan hal berikut:
- Tampilkan DataFrame
- Filter baris yang memiliki usia lebih dari 23
- Urutkan DataFrame berdasarkan kolom `Usia` secara ascending

### 🧠 Latihan 2:
Gunakan DataFrame yang sudah kamu buat, lalu lakukan grouping berdasarkan `Pekerjaan`, dan hitung rata-rata usia untuk setiap pekerjaan.

---

Kalau udah selesai, upload filenya lagi ya. Aku siap bantu review dan kasih saran! 🚀