import streamlit as st

st.set_page_config(page_title="In Progress", layout="centered")
st.title("🏗️ Dev Log")

st.markdown("""       
            
all code is open source! check out my [github](https://github.com/AV-01/Student-Schedule-Website). consider leaving me a star/follow?

working on adding more stuff to this website. however, i'm a one man team and i'm dividing up my focus between other projects, 
so it might take some time until you see changes. here are some of the plans for the future:

## 🎮 version control

**Version 1.0.0** - student directory for 2023-2024, along with filters/search, statistics, and secure storage.
Version 1.0.1 - typo fixes and created "dev log"        
**Version 2.0.0** - added data for additional years, implemented security protocols
Version 2.1.0 - added multiselect features for easier selection

## 🟢 high priority(aka easy stuff)
- ~add data from 2022-2023 and 2024-2025 year!~
- ~add multiselect features~
- more stats for people to analyze
- add buttons for slider(help with page navigation)
- remove "enrichment" from popular classes
            

## 🔴 low priority(aka harder stuff)
- rating system for classes/teachers
- add an "opt out" page for people to remove themselves from the database
- create class rosters so people can see who was in their classes
- setup a form or something so i don't have to keep giving out my discord
                                    
### 🕰️ total hours wasted: 11
""")

st.markdown(
    """
    <div style='text-align: center; margin-top: 2rem; font-size: 0.9rem; color: gray;'>
        Made with ❤️ by <strong>AV</strong>
    </div>
    """,
    unsafe_allow_html=True
)
