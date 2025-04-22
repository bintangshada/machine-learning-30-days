import pandas as pd

data = {
    'Nama': ['Andi', 'Budi', 'Citra', 'Denis', 'Endra'],
    'Usia': [29, 25, 21, 30, 50],
    'Pekerjaan': ['Programmer', 'Designer', 'Manager', 'Designer', 'Designer']
}
df = pd.DataFrame(data)
print(df)

df_filtered = df[df['Usia'] > 23]
print(df_filtered)

df_sorted = df.sort_values(by='Usia', ascending=True)
print(df_sorted)

df_grouped = df.groupby('Pekerjaan')['Usia'].mean()
print(df_grouped)