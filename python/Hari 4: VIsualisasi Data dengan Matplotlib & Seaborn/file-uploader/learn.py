import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Dashboard")

uploaded_file = st.file_uploader("Upload file CSV anda", type="csv")
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write("## Dataset", data.groupby('City'))
else:
    st.info("Upload file CSV terlebih dahulu")