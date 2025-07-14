import streamlit as st

st.set_page_config(page_title="FAQ", layout="centered")
st.title("❓ Frequently Asked Questions")

st.markdown("""
**Q: How do I search for a student?**  
Use the search bar or filters in the sidebar to search by name, grade, teacher, or class.

**Q: Why are some students missing?**  
Make sure your filters aren’t too restrictive.

**Q: How is the data stored?**  
Data is loaded from a JSON file cached in memory for performance. I will not give away the raw data due to privacy concerns. 
            
**Q: I don't want my data here. How do I remove it?**   
I completely understand. I'll create a function that will remove it for you automatically. In the mean time, contact me on discord(**.secretspy**) and I'll remove it.
            
**Q: This data is old. Can you make a new one that's more recent?**     
I would need the data first, which I don't have. If I get my hands on it, maybe...
            
**Q: I have some ideas! Could you add..."**     
I would love to hear your idea! Contact me on discord(**.secretspy**) and I'll get back to u.
""")

st.markdown(
    """
    <div style='text-align: center; margin-top: 3rem; font-size: 0.9rem; color: gray;'>
        Made with ❤️ by <strong>AV</strong>
    </div>
    """,
    unsafe_allow_html=True
)