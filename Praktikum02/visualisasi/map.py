import streamlit as st 
import pandas as pd 
import numpy as np

st.title("Map")
st.write("Kelompok - 20 Visualisasi Data")
st.markdown("""
        1. FAHLIA ATHIYYA MARVA - 0110122176
        2. FAHMI YUSRON FADILLAH - 0110222072
        3. UYUN NILJANAH - 0110222081
""")

df = pd.DataFrame(
    np.random.randn(50, 2)/[10,10] + [15.4589, 75.0078],
    columns=["latitude", "longitude"]
)

st.map(df)

