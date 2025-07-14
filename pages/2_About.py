import streamlit as st

st.set_page_config(page_title="About", layout="centered")
st.title("📘 About This Project")

# st.markdown("""
# This is a searchable directory of students and their schedules built with **Streamlit**.

# - 🔍 Search and filter by name, grade, class, or teacher
# - 💡 Fast filtering with pagination
# - 🌙 Toggle between light and dark modes

# Built by Aryavrat Mishra.
# """)

st.markdown("""            
this is a searchable directory containing all students that go to RHS during the 2023-2024 school year.
at the time im making this(2025), this data is 2 years old and extremeley outdated. 
but, i just happened to have the data and figured i would do something with it.

aside from just being a raw directory, i put in some search and filter features, and a stats page.
                        
made over ~3 hours with python.
            
### check out some of our best graduates
- nihar mudigonda: stanford '28
- giselle kirchner: princeton '28
- simran saluja: upenn '29
- gargi jejurikar: uc berkeley '29
- alex lin: ucla '29
- aryavrat mishra: soon
- and many more...

            
contact me on discord: **.secretspy**

> **"difficult takes a day, impossible takes a week"**
""")


st.markdown(
    """
    <div style='text-align: center; margin-top: 3rem; font-size: 0.9rem; color: gray;'>
        Made with ❤️ by <strong>AV</strong>
    </div>
    """,
    unsafe_allow_html=True
)