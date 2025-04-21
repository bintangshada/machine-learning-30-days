import numpy as np # untuk import dulu NumPy

a = np.array([10, 20, 30, 40, 50])
def rataRata(array):
    jumlah = 0
    for i in range(len(array)):
        jumlah += array[i]
    print(jumlah/len(array))
rataRata(a)
#perhitungan rata rata dengan cara biasa

print(np.mean(a)) #perhitungan dengan lebih singkat menggunakan NumPy
print(np.max(a)) #perhitungan mencari nilai maksimal 
print(np.min(a)) #perhitungan mencari nilai minimum
print(np.std(a)) #perhitungan standar deviasi 

#deviasi sendiri buat ngukur seberapa variatif data tersebut, analoginya standar deviasi kecil biasanya konsisten ngga ada lonjakan atau jarak yang pendek contoh [1,2,1,3], std deviasi yang besar terjadi karena jarak yang jauh seperti [1, 20, 50, 100]

x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

#penjumlahan
print(x+y)

#perkalian elemen
print(x*y)

#dot product
print(x.dot(y))

matrix = np.array([[1,2], [3,4]])

# ukuran array
print(matrix.shape)

# jumlah elemen array
print(matrix.size)

#dimensi array
print(matrix.ndim)
