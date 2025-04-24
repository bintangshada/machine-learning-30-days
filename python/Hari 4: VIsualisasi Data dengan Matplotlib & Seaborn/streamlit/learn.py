import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Judul dashboard
st.title("Dashboard Data Calories")

# Load data
data = pd.read_csv('../data.csv')
st.write('## Dataset', data)

# tampilkan histogram calories
st.write("## Histogram Kalori")
fig, ax = plt.subplots()
ax.hist(data['Calories'], bins=15, color='skyblue')
st.pyplot(fig)
w
# tambahkan filter interaktif
min_cal = int(data['Calories'].min())
max_cal = int(data['Calories'].max())
range_cal = st.slider("Filter Kalori", min_value=min_cal, max_value=max_cal, value=(min_cal, max_cal))

filtered_data = data[(data['Calories'] >= range_cal[0]) & (data['Calories'] <= range_cal[1])]
st.write("### Data Terfilter", filtered_data)