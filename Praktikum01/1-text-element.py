# import library yang dibutuhkan 
import streamlit as st

# Displaying Titlest.title("Praktikum Visualisasi Data Pekan 6")
st.subheader("Praktik Text")

# Displaying Nama Anggota
st.markdown("""
        1. FAHLIA ATHIYYA MARVA - 0110122176
        2. FAHMI YUSRON FADILLAH - 0110222072
        3. UYUN NILJANAH - 0110222081
""")
st.write("Hello")
st.write('World!!!')
st.title("This is our title")
st.header("""This is our Header""")
st.subheader("""This is our sub-header""")
st.caption("""This is our caption""")

# Displaying plain text 
st.text("Hi, \nPeople\t!!!")
st.text("Welcome to")
st.text("""Streamlit's World""")

# Displaying Markdown
st.markdown("# Hi. \n# ***People*** \t !!!!")
st.markdown('## Welcome to')
st.markdown("### Streamlit's World")

# Displaying LaTex
st.latex(r'''cos2\theta =1 -2sin^2\theta''')
st.latex("""(a+b) = a^2 + b^2 + 2ab""")
st.latex(r'''\frac{\partial^2 u}{\partial t}
         = h^2 \left(\frac{\partial^2 u}{\partial x^2}
         + \frac{\partial^2 u}{\partial y^2}
            + \frac{\partial^2 u}{\partial z^2}\right
         )''')

# Displaying python 
st.subheader("Python code")
code = '''
     def hello():
     print("Hello, Streamlit!")
'''
st.code(code, language='python')

# Displaying Java Code
st.subheader("""Java Code""")
st.code("""
public class GFG {
        public static void main string (String arg[])
        {
        System.out.printI("Hello World");
        }
    }
""", language='java')
st.subheader("""Javascript Code""")
st.code(""" <p id="demo"> </p>
        <script>
        try {
        addalert("Welcome Guest!);
        }
        catch(err) {
        document.getElementById("demo").innerHTML = err.message;
        }
        </script> """)


# # MENAMPILKAN RUMUS (LaTeX)
# st.latex(r'''\cos^2\theta = 1-2\sin^2\theta''' ) # rumus trginonmetri
# st.latex(r''' (a+b)^2 = a^2 + b^2 + 2ab ''') # rumis binominal

# # Bagian 3 : Menampilkan kode program 
# st.header("DIsplaying Code")
# st.subheader("Python code")

# # SImpan ke variable
# code = '''
#     def hello():
#     print("Hello, Streamlit!")
# '''

# # st.code() untuk menampilkan potongan kode dnegan format rapi dan syntax highlighting
# st.code(code, language='python')

# st.subheader("Java Code")
# st.code("""
# public class GFG {
#         public static void main string (String arg[])
#     }
# """, language='java')
# # fungsi st.code()bisa digunakan u/ bahasa pemrograman lain speerti Java, python, C++, HTML, dll

# st.subheader("Javascrpt Code")
# st.code("""
# <p> id="demo" </p>
# <script>
#     try {
#         addalert("welcome!"); //kesalahan ketik (addalert)
#         sengaja dibuat untuk menimbulkan error
#     }
#     catch(err) {
#         document.getElementById("Demo").innerHTML = err.message; //
#         menampilkan pesan error di elemen HTML dnegan id 'demo'
#     }
# </script>

# """, language='javascript')
 