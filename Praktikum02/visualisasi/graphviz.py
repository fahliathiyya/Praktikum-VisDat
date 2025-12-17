import streamlit as st 
import pandas as pd 
import numpy as np

st.title("Graphviz Chart")
st.write("Kelompok - 20 Visualisasi Data")
st.markdown("""
        1. FAHLIA ATHIYYA MARVA - 0110122176
        2. FAHMI YUSRON FADILLAH - 0110222072
        3. UYUN NILJANAH - 0110222081
""")

st.graphviz_chart("""
    digraph {
        "Training Data" -> "ML Algorithm"
        "Ml Algorithm" -> "Model" 
        "Model" -> "Results Forecasting"
        "New Data" -> "Model"
        }
""")

