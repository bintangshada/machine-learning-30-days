import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

x = [1,2,3,4]
y = [10, 20, 25, 30]

plt.plot(x, y) # gambar garis dari titik-titik x dan y
plt.title("Contoh Line Plot")
plt.xlabel("X") # label sumbu x
plt.ylabel("Y") # label sumbu y
plt.show() # tampilkan grafik

kategori = ['A', 'B', 'C']
nilai = [10, 20 ,15]

plt.bar(kategori, nilai)
plt.title("Contoh Bar Chart")
plt.show()

data = np.random.randn(100)
plt.hist(data, bins=10)
plt.title("Contoh Histogram")
plt.show()

x = [5,7,8,7,2]
y = [99, 86, 87, 88, 100]

plt.scatter(x,y)
plt.title("Contoh Scatter Plot")
plt.show()


tips = sns.load_dataset('tips')

sns.scatterplot(data=tips, x='total_bill', y='tip')
plt.title("Scatterplot Total Bill vs Tip")
plt.show()