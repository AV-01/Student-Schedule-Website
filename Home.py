import streamlit as st
import json
import math
from datetime import datetime
from azure.storage.blob import BlobServiceClient


st.set_page_config(page_title="Student Directory", layout="wide")

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'user_name' not in st.session_state:
    st.session_state.user_name = ""
if 'user_id' not in st.session_state:
    st.session_state.user_id = ""
if 'expanded_students' not in st.session_state:
    st.session_state.expanded_students = set()

def log_action(user_info, action, details=""):
    """Log user actions to Azure Blob Storage transactions.json"""
    try:
        connection_string = st.secrets['AZURE_STORAGE_CONNECTION_STRING']
        container_name = "personal"
        blob_name = "transactions.json"
        
        blob_service_client = BlobServiceClient.from_connection_string(connection_string)
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
        
        try:
            blob_data = blob_client.download_blob().readall()
            transactions = json.loads(blob_data)
        except Exception:
            transactions = []
        
        new_transaction = {
            "user": user_info,
            "action": action,
            "details": details,
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        transactions.append(new_transaction)
        
        updated_data = json.dumps(transactions, indent=2)
        blob_client.upload_blob(updated_data, overwrite=True)
            
    except Exception as e:
        st.error(f"Logging error: {e}")

def login_form():
    """Display login form and handle authentication"""
    st.title("🔐 Student Directory Login")
    st.markdown("Please enter your credentials to access the student directory.")
    
    passwords = load_passwords()

    with st.form("login_form"):
        first_name = st.text_input("First Name", placeholder="Enter your first name")
        last_name = st.text_input("Last Name", placeholder="Enter your last name")
        student_id = st.text_input("Student ID", placeholder="Enter your student ID number")
        submit_button = st.form_submit_button("Login")

        if submit_button:
            if first_name.strip() and last_name.strip() and student_id.strip():
                input_first = first_name.strip().lower()
                input_last = last_name.strip().lower()
                input_id = student_id.strip()

                matched_user = next(
                    (user for user in passwords
                     if user["first_name"].lower() == input_first
                     and user["last_name"].lower() == input_last
                     and user["student_id"] == input_id),
                    None
                )

                if matched_user:
                    full_name = f"{first_name.strip().title()} {last_name.strip().title()}"
                    user_info = {
                        "first_name": first_name.strip().title(),
                        "last_name": last_name.strip().title(),
                        "student_id": input_id
                    }
                    
                    log_action(user_info, "login", "User successfully logged in")
                    
                    st.session_state.logged_in = True
                    st.session_state.user_name = full_name
                    st.session_state.user_id = input_id
                    st.success("Login successful! Redirecting...")
                    st.rerun()
                else:
                    attempted_user = {
                        "first_name": first_name.strip().title(),
                        "last_name": last_name.strip().title(),
                        "student_id": input_id
                    }
                    log_action(attempted_user, "login_failed", "Invalid credentials provided")
                    st.error("Invalid first name, last name, or student ID.")
            else:
                st.error("Please enter all fields.")

@st.cache_data(ttl="1d")
def load_passwords():
    connection_string = st.secrets['AZURE_STORAGE_CONNECTION_STRING']
    container_name = "personal"
    blob = "passwords.json"

    blob_service_client = BlobServiceClient.from_connection_string(connection_string)

    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob)
    blob_data = blob_client.download_blob().readall()
    password_data = json.loads(blob_data)
    return password_data

@st.cache_data(ttl='1d')
def load_data_from_azure():
    connection_string = st.secrets['AZURE_STORAGE_CONNECTION_STRING']
    container_name = "personal"
    blobs = {
        "22-23": "student_data 22-23.json",
        "23-24": "student_data 23-24.json",
        "24-25": "student_data 24-25.json"
    }

    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    combined_data = []
    
    for year, blob_name in blobs.items():
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
        blob_data = blob_client.download_blob().readall()
        year_data = json.loads(blob_data)
        
        for student in year_data:
            student["year"] = year
        
        combined_data.extend(year_data)
    
    return combined_data

if not st.session_state.logged_in:
    login_form()
else:
    data = load_data_from_azure()
    
    with st.sidebar:
        st.markdown(f"**Welcome, {st.session_state.user_name}!**")
        if st.button("Logout"):
            user_info = {
                "first_name": st.session_state.user_name.split()[0],
                "last_name": st.session_state.user_name.split()[-1],
                "student_id": st.session_state.user_id
            }
            log_action(user_info, "logout", "User logged out")
            
            st.session_state.logged_in = False
            st.session_state.user_name = ""
            st.session_state.user_id = ""
            st.session_state.expanded_students = set()
            st.rerun()
        st.divider()

    with st.sidebar:
        st.title("Filters")

        years = sorted(set(student["year"] for student in data))
        selected_years = st.multiselect("Academic Year(s)", years, default=years)

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
        if student["year"] not in selected_years:
            continue
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

    st.title("📚 Student Directory")
    st.caption(f"Showing {len(visible_students)} of {len(filtered)} result(s)")

    if 'show_schedules' not in st.session_state:
        st.session_state.show_schedules = set()

    if not visible_students:
        st.warning("No students match the current filters.")
    else:
        cols = st.columns(4)
        for i, student in enumerate(visible_students):
            with cols[i % 4]:
                student_key = f"{student['name']}_{student['grade']}_{student.get('student_id', i)}"
                
                st.markdown(f"**{student['name']}** (Grade {student['grade']})")
                
                is_schedule_visible = student_key in st.session_state.show_schedules
                button_text = "Hide Schedule" if is_schedule_visible else "View Schedule"
                
                if st.button(button_text, key=f"btn_{student_key}"):
                    if not is_schedule_visible:
                        user_info = {
                            "first_name": st.session_state.user_name.split()[0],
                            "last_name": st.session_state.user_name.split()[-1],
                            "student_id": st.session_state.user_id
                        }
                        
                        log_action(
                            user_info, 
                            "schedule_access", 
                            f"Accessed schedule for {student['name']} (Grade {student['grade']}, ID: {student.get('student_id', 'N/A')})"
                        )
                    
                    if student_key in st.session_state.show_schedules:
                        st.session_state.show_schedules.remove(student_key)
                    else:
                        st.session_state.show_schedules.add(student_key)
                
                if student_key in st.session_state.show_schedules:
                    with st.container():
                        st.markdown("**Schedule:**")
                        for period, info in sorted(student["periods"].items(), key=lambda x: int(x[0])):
                            st.markdown(
                                f"- **Period {period}**: `{info['class_name']}`  \n"
                                f"&nbsp;&nbsp;&nbsp;&nbsp;📍 **Room**: `{info['room_num']}`  \n"
                                f"&nbsp;&nbsp;&nbsp;&nbsp;👨‍🏫 **Teacher**: `{info['teacher_name'].strip()}`"
                            )
                
                st.divider()
