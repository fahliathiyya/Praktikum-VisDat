import streamlit as st 
import pandas as pd 
import numpy as np

st.title("Line Chart")
st.write("Kelompok - 20 Visualisasi Data")
st.markdown("""
        1. FAHLIA ATHIYYA MARVA - 0110122176
        2. FAHMI YUSRON FADILLAH - 0110222072
        3. UYUN NILJANAH - 0110222081
""")

df = pd.DataFrame(
    np.random.randn(40, 4),
    columns=["C1", "C2", "C3", "C4"]
)
st.line_chart(df)

