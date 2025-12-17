import streamlit as st
import pandas as pd     # untuk mengelola data dalam bentuk tabel (dataframe)
import numpy as np      # data numerik acak
import altair as alt    # data chart interaktif

st.header("Praktikum VisDat")
st.subheader("Data Element")
st.markdown("""
        - KELOMPOK 20 
        1. FAHLIA ATHIYYA MARVA - 0110122176
        2. FAHMI YUSRON FADILLAH - 0110222072
        3. UYUN NILJANAH - 0110222081
""")

# defining random values in a dataframe using pandas and numpy
st.subheader("Random values in table")
df = pd.DataFrame(
    np.random.randn(30, 10),
    columns=('col_no %d' %i for i in range (10)))
st.dataframe(df)

# highlighting minimun value objects
st.subheader("Highlight Minimun Value")
st.dataframe(df.style.highlight_min(axis=0))

# defining data in table
st.subheader("Static Table")
st.table(df)

# Defining Metrics
st.subheader("Metrics")
st.metric(label="temperature", value="31 C", delta="1.2 C")
# Defining Columns
col1, col2, col3 = st.columns(3)
col1.metric("Curah hujan", "100 cm", "10 cm")
col2.metric(label="populasi", value="123 miliar", delta="1 miliar", delta_color="inverse")
col3.metric(label="Pelanggan", value=100, delta=10, delta_color="off")

st.metric(label="Speed", value=None, delta=0)
st.metric("Trees", "91456", "-1132649")

# defining multi arguments in write function 
st.write('Here is our Data', df, 'Data is in dataframe format. \n', "\nWrite is Super function")

df = pd.DataFrame(
    np.random.randn(10, 2),
    columns=['a','b'])

# defining chart
chart = alt.Chart(df).mark_bar().encode(
    x='a', y='b', tooltip=['a', 'b'])
st.write(chart)

# # dataframe : 
# st.subheader("DataFrame")

# df = pd.DataFrame(
#     np.random.randn(30,10),
#     columns=('col_no %d' % i for i in range (10))
# )

# # menampilkan dataframe
# st.dataframe(df)

# # highlight nilai minimum 
# st.subheader("highlight minumum value di dataframe")

# # highlight nilai terkecil di setiap kolom dataframe
# # axis=0 bekerja per kolom
# st.dataframe(df.style.highlight_min(axis=0))

# # highlight nilai terbesar di setiap kolom dataframe
# # axis=0 bekerja per kolom
# st.subheader("highlight maximum value di dataframe")
# st.dataframe(df.style.highlight_max(axis=0))

# # table statis
# st.subheader("Table Statis")

# df = pd.DataFrame(
#     np.random.randn(30,10),
#     columns=('col_no %d' % i for i in range (10))
# )
# st.table(df)

# # Metrics: komponen tampilan angka penting
# st.subheader("Metrics")

# # menampilkan metrics tunggal (nilai utama + perubahan nilai)
# st.metric(label="temperature", value="31 C", delta="1.2 C")

# # metric sesuai delta_color
# # delta_color digunakan untuk memberi warna sesuai arah perubahan 
# # 

# col1, col2, col3 = st.columns(3)

# col1.metric("Curah hujan", "100 cm", "10 cm")
# col2.metric(label="populasi", value="123 miliar", delta="1 miliar", delta_color="inverse")
# col3.metric(label="Pelanggan", value=100, delta=10, delta_color="off")

# st.metric(label="Speed", value=None, delta=0)
# st.metric("Trees", "91456", "-1132649")

# df = pd.DataFrame(
# np.random.randn(30, 10),
# columns=('col_no %d' % i for i in range (10)))
# # defining multi arguments in write function 
# st.write('Here is our data', df, 'Data is in dataframe format.\n', "\nWrite is Super function")

# # defining random values for chart
# df = pd.DataFrame(
#     np.random.randn(10,2),
#     columns=['a','b'])

# # defining chart 
# chart = alt.chart(df).mark_bar().encode(
#     x='a', y='b', tooltip=['a', 'b'])

# # defining chart in write() function 
# st.write(chart)