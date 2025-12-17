import streamlit as st 
import time         

st.title("Praktikum 4 - Visualisasi Data")
st.caption("Bagian 4: Button Sliders")

st.markdown("""
1. FAHLIA ATHIYYA MARWA - 0110122176 
2. FAHMI YUSRON FADILLAH - 0110222072
3. UYUN NILJANAH - 0110222081
 """)

# Buttons
st.title('Creating a Button') 
# Defining a Button
button = st.button('Click Here')
if button:
    st.write('Youn Have Klicked the Button')
else:
    st.write('You Hane Not Clicked the Button')

#Radio Button 
st.title('Creating Radio Button')

#Defining Radio Button
gender = st.radio( 
    "Select your gender",
    ('Male', 'Female', 'Others'))
if gender == 'Male':
    st.write('You Have Selected Male')
elif gender == 'Female':
    st.write('You Have Selected Female')
else:
    st.write('You Have Selected Others')

#Check Boxes
st.title('Creating Checkboxes')
st.write('select Your Hobies:')
 
# Defining Checkboxes
check_1 = st.checkbox('Books')
check_2 = st.checkbox('Movies')
check_3 = st.checkbox('Sports')

#Drop-Downs
st.title('Creating Dropdown')

# Creating Dropdown
hobby = st.selectbox('Choose your hobby:',
('Books', 'Movies', 'Sports'))

#Multiselects
st.title('Multi-Select')

# Defining Multi_Select with Pre-Selection
hobbies = st.multiselect(
    'Where are you Hobbies',
    ['Reading', 'Cooking', 'Watching Movies/TV Series', 'Playing', 'Drawing', 'Hiking'],
    ['Reading', 'Playing'])

#Download Buttons
st.title('Download Button')
# Creating Download Button
down_btn = st.download_button(
    label="Download Book",
    data = open("C:\VISUALISASI DATA\Dokumen\Image Book.png", "rb"),
    file_name="Image.jpeg",
    mime="image/jpg"
)

#Progress Bars
st.title('Progress Bar')

# Defino=inf Progress Bar
download = st.progress(0)
for percentage in range(100):
    time.sleep(0.1)
    download.progress(percentage+1)
st.write('Download Complete')

#Spinners
st.title('Spinner')

# Defining Spinner
with st.spinner('Loading...'):
    time.sleep(5)
st.write('Hello Data Scientists')