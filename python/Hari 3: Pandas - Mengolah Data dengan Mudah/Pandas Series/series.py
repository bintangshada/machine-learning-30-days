import pandas as pd
import numpy as np

#Soal 1: Membuat series sederhana
data = pd.Series([100, 200, 300, 400, 500])
print(data)
print(data.iloc[2])
print(np.mean(data))

#Soal 2: Series dengan Index Custom

a = [85, 90, 75]
data1 = pd.Series(a, index=['A001', 'A002', 'A003'])
print(data1)
print(data1['A002'])
print(np.max(a))
print(np.min(a))

#Soal 3: Gunakan apply() pada Series
nilai = pd.Series([80, 60, 90, 50, 100])

nilai.apply(lambda x: print(x,': Lulus') if x >= 70 else print(x,': Tidak Lulus'))

#Soal 4: Filter Series tampilkan hanya nilai yang lebih besar drpd 70

def kkm(n):
    for i in range(len(n)):
         if n[i] > 70:
            print(n[i])

kkm(nilai)