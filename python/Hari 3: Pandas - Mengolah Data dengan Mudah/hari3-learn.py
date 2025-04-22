import pandas as pd
# jika error module tidak ada bisa download dulu dengan pip install wheel + pip install pandas
data = {
    'Nama': ['Alice', 'Bob', 'Charlie'],
    'Usia': [25, 30, 35],
    'Kota': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)

print(df) #tampilkan semua data
print(df['Nama']) #tampilan kolom nama
print(df[['Nama','Usia']]) #tampilkan kolom nama dan usia

#akses baris tertentu
print(df.iloc[0]) #baris pertama

print(df.loc[1]) # index pertama

csv = pd.read_csv('data.csv')
print(csv.head()) #tampilkan 5 baris pertama

#sorting data
df_sorted = df.sort_values(by='Usia', ascending=False)
print(df_sorted)

#filter data
df_filtered = df[df['Usia']> 30]
print(df_filtered)

#grouping data
dataNilai = {
    'Kategori': ['A', 'B', 'A', 'B'],
    'Nilai': [10, 20, 30, 40]
}

dfNilai = pd.DataFrame(dataNilai)

print(dfNilai)

dfGrouped = dfNilai.groupby('Kategori')['Nilai'].mean()
print(dfGrouped)