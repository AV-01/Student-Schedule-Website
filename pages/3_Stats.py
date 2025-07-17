import streamlit as st
import json
import pandas as pd
from collections import Counter
import plotly.express as px
from azure.storage.blob import BlobServiceClient

st.set_page_config(page_title="Stats", layout="wide")
st.title("📊 School Stats")

@st.cache_data
def load_data_from_azure():
    connection_string = st.secrets['AZURE_STORAGE_CONNECTION_STRING']
    container_name = "personal"
    blob_name = "student_data 23-24.json"

    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)

    blob_data = blob_client.download_blob().readall()
    return json.loads(blob_data)

data = load_data_from_azure()

total_students = len(data)

grade_counts = Counter(student["grade"] for student in data)
grade_df = pd.DataFrame(grade_counts.items(), columns=["Grade", "Count"]).sort_values("Grade")

class_counts = Counter(
    info["class_name"].strip()
    for student in data
    for info in student["periods"].values()
)
top_classes = class_counts.most_common(7)
class_df = pd.DataFrame(top_classes, columns=["Class", "Count"])

teacher_counts = Counter(
    info["teacher_name"].strip()
    for student in data
    for info in student["periods"].values()
)
top_teachers = teacher_counts.most_common(10)
teacher_df = pd.DataFrame(top_teachers, columns=["Teacher", "Count"])

col1, col2, col3 = st.columns(3)
col1.metric("Total Students", total_students)
col2.metric("Unique Classes", len(class_counts))
col3.metric("Unique Teachers", len(teacher_counts))

st.divider()

st.subheader("Students per Grade")
st.plotly_chart(px.bar(grade_df, x="Grade", y="Count", color="Grade", title="Student Count by Grade"))

st.subheader("Top 7 Most Popular Classes")
st.plotly_chart(px.pie(class_df, names="Class", values="Count", title="Class Distribution"))

st.subheader("Top 10 Teachers by Student Count")
st.plotly_chart(px.bar(teacher_df, x="Count", y="Teacher", orientation="h", title="Most Popular Teachers"))

st.markdown(
    """
    <div style='text-align: center; margin-top: 2rem; font-size: 0.9rem; color: gray;'>
        Made with ❤️ by <strong>AV</strong>
    </div>
    """,
    unsafe_allow_html=True
)
