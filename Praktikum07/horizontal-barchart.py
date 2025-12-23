import streamlit as st 
import matplotlib.pyplot as plt 
import numpy as np 

# judul 
# header 
st.title("Praktikum 07 Visualisasi Data")
st.write("Kelompok 20")
st.markdown("""
    1. FAHLIA ATHIYYA MARVA - 0110122176
    2. FAHMI YUSRON FADILLAH - 0110222072
    3. UYUN NILJANAH - 0110222081
""")

# dataset 
brands = ['Brand A', 'brand B', 'brand C', 'brand D']
sales_2023 = [350, 420, 300, 200]
sales_2024 = [380, 450, 420, 300]

# atur posisi Y
y = np.arange(len(brands))
bar_width = 0.4

# filter kategori 
kategori = st.selectbox(
    "Pilih Kategori visualisasi",
    ['Basic Bar Chart', 'Kustomisasi grafik', 'Multiple Chart']
)

# basic bar chart 
if kategori == "Basic Bar Chart":
    st.subheader("Horizontal Bar Chart Sederhana")


    # stacked
    st.subheader("Stacked Horizontal Bar Chart Sederhana")

    fig2, ax2, = plt.subplots()

    ax2.set_yticks(y)
    ax2.set_yticklabels(brands)
    ax2.set_title("Horizontal Bar Chart - 2023")
    ax2.set_xlabel('JUmlah Penjualan')
    ax2.set_ylabel('Merk')
    ax2.barh(y, sales_2023, color='skyblue', label='2023')
    ax2.barh(y, sales_2024, color='lightgreen', label='2024', left=sales_2023)
    ax2.legend()


    st.pyplot(fig2)

# kustomisasi 
elif kategori == "Kustomisasi grafik" :
    st.subheader("Kustomisasi Horizontal Bar Chart")
    fig3, ax3, = plt.subplots()

    # grafik batang horizontal 
    ax3.set_yticks(y)
    ax3.set_yticklabels(brands)
    ax3.set_title("HKustomisasi Horizontal Bar Chart - 2023")
    ax3.set_xlabel('JUmlah Penjualan')
    ax3.set_ylabel('Merk')
    ax3.barh(y, sales_2023, color='skyblue', edgecolor='black')
    ax3.grid(axis='x', linestyle='--', alpha=0.6)

    # label nilai
    for i, v in enumerate(sales_2023):
        ax3.text(v+5, i, str(v), va='center')
    st.pyplot(fig3)

    st.subheader("Customized Stacked Horizontal Bar Chart")

    fig4, ax4 = plt.subplots()
    ax4.barh(y, sales_2023, label='2023', color='skyblue', edgecolor='black')
    ax4.barh(y, sales_2024, left=sales_2023, label='2024', color='salmon', edgecolor='black')
    ax4.set_yticks(y)
    ax4.set_yticklabels(brands)
    ax4.set_xlabel("Total Sales (in Units)")
    ax4.set_title("Customized Stacked Sales by Brand")
    ax4.legend()
    ax4.grid(axis='x', linestyle='--', alpha=0.6)

    st.pyplot(fig4)

    # MULTIPLE CHART
else:
    st.subheader("Multiple Horizontal Bar Chart")

    fig5, ax5 = plt.subplots()
    ax5.barh(y - bar_width/2, sales_2023, height=bar_width, label='2023')
    ax5.barh(y + bar_width/2, sales_2024, height=bar_width, label='2024')
    ax5.set_yticks(y)
    ax5.set_yticklabels(brands)
    ax5.set_xlabel("Total Sales (in Units)")
    ax5.set_title("Multiple Horizontal Bar Chart")
    ax5.legend()
    st.pyplot(fig5)

    st.subheader("Multiple Stacked Horizontal Bar Chart")

    fig6, ax6 = plt.subplots()
    ax6.barh(y, sales_2023, label='2023')
    ax6.barh(y, sales_2024, left=sales_2023, label='2024')
    ax6.set_yticks(y)
    ax6.set_yticklabels(brands)
    ax6.set_xlabel("Total Sales (in Units)")
    ax6.set_title("Multiple Stacked Horizontal Bar Chart")
    ax6.legend()
    st.pyplot(fig6)

    



