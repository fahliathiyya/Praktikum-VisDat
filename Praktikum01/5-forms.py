import streamlit as st 
import datetime
import pandas as pd 

st.header("Praktikum VisDat")
st.subheader("Forms")
st.markdown("""
        - KELOMPOK 20 
        1. FAHLIA ATHIYYA MARVA - 0110122176
        2. FAHMI YUSRON FADILLAH - 0110222072
        3. UYUN NILJANAH - 0110222081
""")

st.title("Text Box")
# Creating Text box
name = st.text_input("Enter Your Name")
st.write("Your Name is", name)
# Creating text box with 10 as char limit
name = st.text_input("Enter your name", max_chars=10)
# Creating password text box
password = st.text_input("Enter your passsword", type='password')

st.title("Text Area")
# creating text area
input_text = st.text_area("Enter your review")
# printing enterd text 
st.write("""You entered: \n""", input_text)

st.title("Number Input")
# number input 
# create number input 
st.number_input("enter your number")
# create number input 
num = st.number_input("enter your number", 0, 10, 5, 2)
st.write("Min. value is 0, \n Max. Value is 10")
st.write("default value is 5, \n step size value is 2")
st.write("total value after adding number entered with step value is:", num)

st.title("Time")
# defining time function 
st.time_input("Select your time")

st.title("Date")
# defining date function 
st.date_input("Select Date", value=datetime.date(1989, 12, 25),
min_value=datetime.date(1987,1,1),
max_value=datetime.date(2005,12,1)
)

st.title("Select Color")
# defining color picker
color_code = st.color_picker("Select yout color")
st.header(color_code)

st.title("Dataset Upload")
st.title("CSV Data")
data_file = st.file_uploader("Upload CSV", type=["csv"])
details = st.button("Check Details")
if details:
    if data_file is not None:
        file_details = {"file_name":data_file.name, "file_type":data_file.type, "file_size":data_file.size}
        st.write(file_details)
        df = pd.read_csv(data_file)
        st.dataframe(df)
    else:
        st.write("No CSV File is Uploaded")
