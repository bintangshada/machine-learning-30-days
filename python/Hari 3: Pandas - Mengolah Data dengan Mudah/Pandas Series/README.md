Nice catch! 💯 Kamu jeli banget — sekarang aku akan jelaskan juga tentang **`Series`** di Pandas, biar kamu benar-benar paham semuanya dari dasar.

---

## 📌 Apa Itu `Series`?

### 🔹 Definisi:
**`Series`** adalah **struktur data 1 dimensi** di Pandas — mirip seperti **list** di Python, tapi dengan **label/index** untuk setiap elemennya.

---

### 🔸 Contoh:
```python
import pandas as pd

s = pd.Series([10, 20, 30])
print(s)
```

**Output:**
```
0    10
1    20
2    30
dtype: int64
```

> 👉 Ini adalah **Series** dengan index `[0, 1, 2]` dan nilai `[10, 20, 30]`.

---

### 🔹 Dibandingkan dengan `list`:
```python
list_biasa = [10, 20, 30]
```
- Tidak punya label/index yang terlihat (walaupun sebenarnya pakai angka otomatis)
- Tidak punya tipe data bawaan (`dtype`)

---

## 📦 Dimana Series Digunakan?
- **Setiap kolom dalam DataFrame itu adalah Series.**
  
Contoh:
```python
df = pd.DataFrame({
    'Usia': [25, 30, 35]
})

print(type(df['Usia']))  # <class 'pandas.core.series.Series'>
```

> `df['Usia']` adalah **Series**!

---

## 💡 Kenapa Series Penting?
Karena kita sering banget:
- Menerapkan fungsi ke satu kolom → pakai `.apply()`
- Melakukan operasi matematis kolom demi kolom
- Filter dengan kondisi seperti: `df[df['Usia'] > 30]`

---

## ✨ Analogi Simpel
| Tipe Data | Bentuk      | Contoh                      |
|-----------|-------------|-----------------------------|
| `list`    | 1 dimensi   | `[1, 2, 3]`                 |
| `Series`  | 1 dimensi   | `0: 1, 1: 2, 2: 3` (berlabel)|
| `DataFrame`| 2 dimensi  | Tabel (baris × kolom)       |

---

Kalau kamu mau, aku bisa kasih latihan kecil khusus tentang Series juga! Mau dicoba? 😄

Keren! Yuk kita latihan ringan tentang **Pandas Series**, biar makin paham penggunaannya dari dasar sampai aplikatif 🚀

---

## 🧠 **Latihan Dasar Series**

### ✅ **Soal 1: Membuat Series Sederhana**
Buat Series berisi nilai-nilai berikut: `[100, 200, 300, 400, 500]`, lalu:
- Tampilkan Series-nya
- Tampilkan nilai pada indeks ke-2
- Tampilkan rata-rata nilainya

---

### ✅ **Soal 2: Series dengan Index Custom**
Buat Series seperti ini:

| Kode  | Nilai |
|-------|-------|
| A001  | 85    |
| A002  | 90    |
| A003  | 75    |

- Buat Series-nya dengan index custom (kode-kode di atas)
- Tampilkan nilai dari kode `A002`
- Hitung nilai maksimum dan minimum

---

### ✅ **Soal 3: Gunakan apply() pada Series**
Diberikan Series:
```python
nilai = pd.Series([80, 60, 90, 50, 100])
```
- Gunakan `.apply()` dengan `lambda` untuk mengubah nilai menjadi:
  - `"Lulus"` jika nilai ≥ 70
  - `"Tidak Lulus"` jika nilai < 70

---

### ✅ **Bonus Soal 4: Filter Series**
Dengan Series yang sama seperti di soal 3:
- Tampilkan hanya nilai yang lebih besar dari 70

---

## 📩 Cara Kirim
Kamu bisa kerjakan di file `.py` seperti biasa, lalu upload untuk aku review dan kasih feedback ✨

Siap latihan? Kalau butuh contoh juga, tinggal bilang ya!