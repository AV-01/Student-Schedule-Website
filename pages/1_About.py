import streamlit as st

st.set_page_config(page_title="About", layout="centered")
st.title("About")

st.markdown("""            
this is a searchable directory containing all students that went to RHS from 2022 to 2025.
this is the best available, open source directory out there. within one search, you can find anyone you're looking for.

aside from just being a raw directory, i put in some search and filter features, and a stats page. more features to come soon!
                        
made entirely with python.
""")

# Features section
st.markdown("## Features")
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    - 🔍 **Search** by name or student ID
    - 🎯 **Filters** for grade, class, and teacher
    - 📄 **Pagination** for fast rendering
    - 📊 **Statistics dashboard** with charts
    """)

with col2:
    st.markdown("""
    - 🔐 **Required login** (RHS students only)
    - ☁️ **Secure cloud storage** with Azure
    - 📱 **Multipage layout** for easy navigation
    - 🔓 **Open source** code on GitHub
    """)

# Hall of fame section
st.markdown("## 🎓 Check Out Some of Our Best Graduates")
st.markdown("""
- christopher franco: mit '27
- sunny liu: harvard '27  
- nihar mudigonda: stanford '28
- giselle kirchner: princeton '28
- simran saluja: upenn '29
- gargi jejurikar: uc berkeley '29
- alex lin: ucla '29
- mateo lopez: uchicago '29
- aryavrat mishra: soon
- and many more...
""")

# Contact and links
# st.markdown("## 📞 Contact & Links")
# col1, col2 = st.columns(2)

# with col1:
# st.markdown("Contact me on **Discord:** .secretspy")


st.markdown("---")
st.markdown("Contact me on **Discord:** .secretspy")
st.markdown("> **\"difficult takes a day, impossible takes a week\"** ")

st.markdown(
    """
    <div style='text-align: center; margin-top: 3rem; font-size: 0.9rem; color: gray;'>
        Made with ❤️ by <strong>AV</strong>
    </div>
    """,
    unsafe_allow_html=True
)