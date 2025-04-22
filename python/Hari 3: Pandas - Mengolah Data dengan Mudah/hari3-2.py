import pandas as pd
import numpy as np

data = pd.read_csv('data.csv')
print(data)

#soal 1 baca file dan tampilkan 10 baris pertamanya saja

print(data.head(10))

#soal 2 tampilkan semua data dengan pulse > 110 dan calories > 400

print(data[(data['Pulse']>110) & (data['Calories']>400)])

#soal 3 urutkan data berdasarkan Maxpulse secara menurun

print(data.sort_values(by='Maxpulse', ascending=True)) #salah harusnya False

# soal 4 hitung statistik deskriptif dari kolom Calories
print(f"Mean: {np.mean(data['Calories'])}\nMax: {np.max(data['Calories'])}\nMin: {np.min(data['Calories'])}\nStandard Deviation: {np.std(data['Calories'])}")

# soal 5 kelompokan data berdasarkan Duration, lalu hitung rata-rata Calories untuk tiap durasi
print(data.groupby('Duration')['Calories'].mean())


#revisi

#soal 3 urutkan data berdasarkan Maxpulse secara menurun
print(data.sort_values(by='Maxpulse', ascending=False))

# soal bonus challenge lanjutan

#tambahkan kolom Katergori kalori dengan aturan Calories >= 400 ->"Tinggi" Calories < 400 -> "Rendah"

data["Kategori Kalori"] = data['Calories'].apply(lambda x: 'Tinggi' if x >= 400 else 'Rendah')
print(data[['Calories', 'Kategori Kalori']])
