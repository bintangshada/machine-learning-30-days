import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# 📥 1. Load Data
data = pd.read_csv("data.csv")
print("Data Awal:")
print(data.head())

# 🔍 2. Cek Missing Value
print("\nCek Missing Value:")
print(data.isnull().sum())

# ✅ 3. Isi Missing Value dengan Rata-rata (jika ada)
data_filled = data.fillna(data.mean(numeric_only=True))
print("\nData Setelah Mengisi Missing Value:")
print(data_filled.head())

# 🎯 4. Pisahkan Fitur dan Target (Calories jadi target)
X = data_filled.drop("Calories", axis=1)
y = data_filled["Calories"]

print("\nFitur (X):")
print(X.head())
print("\nTarget (y):")
print(y.head())

# ✂️ 5. Split Data (80% Train, 20% Test)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(f"\nJumlah data latih: {len(X_train)}")
print(f"Jumlah data uji: {len(X_test)}")

# 📏 6. Standardisasi Fitur
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("\nContoh X_train setelah distandardisasi:")
print(X_train_scaled[:5])
