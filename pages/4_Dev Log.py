import streamlit as st

st.set_page_config(page_title="In Progress", layout="centered")
st.title("🏗️ Dev Log")

st.markdown("""       
            
all code is open source! check out my [github](https://github.com/AV-01/Student-Schedule-Website). consider leaving me a star/follow?

working on adding more stuff to this website. however, i'm a one man team and i'm dividing up my focus between other projects, 
so it might take some time until you see changes. here are some of the plans for the future:
            
## 🟢 high priority(aka easy stuff)
- add data from 2022-2023 and 2024-2025 year!
- more stats for people to analyze
- add buttons for slider(help with page navigation)
- remove "enrichment" from popular classes
            

## 🔴 low priority(aka harder stuff)
- rating system for classes/teachers
- add an "opt out" page for people to remove themselves from the database
- setup a form or something so i don't have to keep giving out my discord
                                    
### 🕰️ total hours wasted: 5
""")

st.markdown(
    """
    <div style='text-align: center; margin-top: 2rem; font-size: 0.9rem; color: gray;'>
        Made with ❤️ by <strong>AV</strong>
    </div>
    """,
    unsafe_allow_html=True
)
