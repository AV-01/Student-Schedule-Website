import streamlit as st
import json
import math
from azure.storage.blob import BlobServiceClient


st.set_page_config(page_title="Student Directory", layout="wide")

# @st.cache_data
# def load_data():
#     with open("student_data.json") as f:
#         return json.load(f)

# data = load_data()

@st.cache_data
def load_data_from_azure():
    connection_string = st.secrets['AZURE_STORAGE_CONNECTION_STRING']
    container_name = "personal"
    blob_name = "student_data.json"

    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)

    blob_data = blob_client.download_blob().readall()
    return json.loads(blob_data)

data = load_data_from_azure()

test

with st.sidebar:
    st.title("Filters")
    # st.session_state.dark_mode = st.checkbox("🌙 Dark Mode", value=st.session_state.dark_mode)

    # grades = sorted(set(student["grade"] for student in data))
    grades = ['8', '9', '10', '11', '12']
    teachers = sorted({info["teacher_name"].strip() for student in data for info in student["periods"].values()})
    classes = sorted({info["class_name"].strip() for student in data for info in student["periods"].values()})

    selected_grade = st.selectbox("Grade", ["All"] + grades)
    selected_class = st.selectbox("Class Name", ["All"] + classes)
    selected_teacher = st.selectbox("Teacher", ["All"] + teachers)
    query = st.text_input("Search name")

    st.markdown(
    """
    <div style='text-align: center; margin-top: 3rem; font-size: 0.9rem; color: gray;'>
        Made with ❤️ by <strong>AV</strong>
    </div>
    """,
    unsafe_allow_html=True
    )

filtered = []
for student in data:
    if query.lower() not in student["name"].lower():
        continue
    if selected_grade != "All" and student["grade"] != selected_grade:
        continue
    if selected_class != "All" and all(info["class_name"].strip() != selected_class for info in student["periods"].values()):
        continue
    if selected_teacher != "All" and all(info["teacher_name"].strip() != selected_teacher for info in student["periods"].values()):
        continue
    filtered.append(student)

students_per_page = 12
total_pages = math.ceil(len(filtered) / students_per_page)
try:
    current_page = st.slider("Page", 1, total_pages, 1)
except:
    current_page = st.slider("Page", 1, 2, 1)
start_idx = (current_page - 1) * students_per_page
end_idx = start_idx + students_per_page
visible_students = filtered[start_idx:end_idx]

st.title("📚 Student Directory(2023-2024)")
st.caption(f"Showing {len(visible_students)} of {len(filtered)} result(s)")

if not visible_students:
    st.warning("No students match the current filters.")
else:
    cols = st.columns(4)
    for i, student in enumerate(visible_students):
        with cols[i % 4]:
            with st.expander(f"{student['name']} (Grade {student['grade']})", expanded=False):
                # st.markdown(f"**ID**: `{student['student_id']}`")
                st.markdown("**Schedule:**")
                for period, info in sorted(student["periods"].items(), key=lambda x: int(x[0])):
                    st.markdown(
                        f"- **Period {period}**: `{info['class_name']}`  \n"
                        f"&nbsp;&nbsp;&nbsp;&nbsp;📍 **Room**: `{info['room_num']}`  \n"
                        f"&nbsp;&nbsp;&nbsp;&nbsp;👨‍🏫 **Teacher**: `{info['teacher_name'].strip()}`"
                    )

# if st.session_state.dark_mode:
#     st.markdown(
#         """
#         <style>
#         body {
#             background-color: #0e1117;
#             color: #cfcfcf;
#         }
#         </style>
#         """, unsafe_allow_html=True
#     )
