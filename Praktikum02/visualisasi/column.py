import streamlit as st 
import pandas as pd 
import numpy as np

st.title("Columns Chart")
st.write("Kelompok - 20 Visualisasi Data")
st.markdown("""
        1. FAHLIA ATHIYYA MARVA - 0110122176
        2. FAHMI YUSRON FADILLAH - 0110222072
        3. UYUN NILJANAH - 0110222081
""")

col1, col2 = st.columns(2)

col1.write("Ini adalah kolom pertama")
col2.write("ini adalah kolom kedua")




