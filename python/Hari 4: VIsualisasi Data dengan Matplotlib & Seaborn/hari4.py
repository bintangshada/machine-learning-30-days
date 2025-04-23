import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#soal 1
x = [1,2,3,4,5]
y = [10,12,15,20,30]

plt.plot(x, y)
plt.title("Line Plot")
plt.xlabel('X')
plt.ylabel('Y')
plt.show()

#soal 2
kategori = ['A', 'B', 'C', 'D']
nilai = [5, 10, 15, 7]

plt.bar(kategori, nilai)
plt.title("Bar Chart")
plt.show()

#soal 3
data = np.random.randn(100)
plt.hist(data, bins=15)
plt.title("Histogram")
plt.show()

#soal 4
x = [1,2,3,4,5]
y = [5,4,3,2,1]

plt.scatter(x,y)
plt.title("Scatter plot")
plt.show()

#soal 5
data = pd.read_csv('data.csv')

plt.hist(data['Calories'], bins=15)
plt.title("Calories")
plt.xlabel("Calories")
plt.ylabel("Jumlah Data")
plt.show()