import streamlit as st

st.set_page_config(page_title="About", layout="centered")
st.title("📘 About This Project")

st.markdown("""            
this is a searchable directory containing all students that went to RHS during from 2023 to 2024.
the data is 2 years old, but i just got the data for a couple other years, so i will implement those. 

aside from just being a raw directory, i put in some search and filter features, and a stats page.
                        
made over ~3 hours with python.
            
### check out some of our best graduates
- sunny liu: harvard '27 (she's not in the directory yet)
- nihar mudigonda: stanford '28
- giselle kirchner: princeton '28
- simran saluja: upenn '29
- gargi jejurikar: uc berkeley '29
- alex lin: ucla '29
- mateo lopez: uchicago '29
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