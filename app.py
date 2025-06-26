# app.py
import streamlit as st
from utils import (
    get_condition_info,
    suggest_conditions,
    generate_treatment_guidance,
    assess_emergency,
    get_sample_patient_data,
    generate_ai_chat_response
)

st.set_page_config(
    page_title="HealthAI: Intelligent Healthcare Assistant",
    page_icon="⚕️",
    layout="wide"
)

st.markdown("""
<style>
    .main { background-color: #f8f9fa; padding: 20px; }
    .sidebar { background-color: #e6f2ff; }
    h1 { color: #2c3e50; border-bottom: 2px solid #2980b9; padding-bottom: 10px; }
    .stButton>button { background-color: #2980b9; color: white; }
    .condition-card {
        background-color: #e8f5e9;
        padding: 15px;
        border-radius: 5px;
        margin: 10px 0;
    }
    .stTextInput>div>div>input { border: 1px solid #2980b9; }
</style>
""", unsafe_allow_html=True)

if 'current_view' not in st.session_state:
    st.session_state.current_view = "Home Page"
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Sidebar
st.sidebar.header("👤 Patient Profile")
name = st.sidebar.text_input("Full Name")
age = st.sidebar.number_input("Age", 0, 120, 30)
gender = st.sidebar.selectbox("Gender", ["Male", "Female", "Other"])
st.sidebar.text_area("Medical History")

# Main Title
st.title("⚕️ HealthAI: Intelligent Healthcare Assistant")
view_options = ["Home Page", "Patient Chat", "Disease Prediction", "Treatment Plans", "Health Analytics"]
current_view = st.radio("Navigation", view_options, horizontal=True, label_visibility="hidden")

# Home Page
if current_view == "Home Page":
    st.subheader("Welcome to Your Health Assistant")
    st.markdown("""
    **How can I help you today?**
    - Chat about your health concerns
    - Check possible conditions based on symptoms
    - Get treatment recommendations
    - Track your health measurements
    """)
    # Removed broken image permanently

# Patient Chat
elif current_view == "Patient Chat":
    st.subheader("HealthAI Chat Assistant")
    if not st.session_state.chat_history:
        st.session_state.chat_history.append({"role": "assistant", "content": "Hello! I'm your HealthAI assistant. How can I help you today?"})

    for msg in st.session_state.chat_history:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    if prompt := st.chat_input("Type your health question..."):
        st.session_state.chat_history.append({"role": "user", "content": prompt})
        with st.chat_message("assistant"):
            response = generate_ai_chat_response(prompt)
            st.markdown(response)
            st.session_state.chat_history.append({"role": "assistant", "content": response})

# Disease Prediction
elif current_view == "Disease Prediction":
    st.subheader("Symptom Checker")
    symptoms = st.text_area("Describe all your symptoms in detail:", height=150)

    if st.button("Analyze Symptoms"):
        if symptoms:
            emergency = assess_emergency(symptoms)
            if emergency["emergency"]:
                st.error(f"🚨 EMERGENCY: {emergency['message']}")

            conditions = suggest_conditions(symptoms)
            if conditions:
                st.info("Possible conditions based on your symptoms:")
                for condition in conditions[:5]:
                    info = get_condition_info(condition)
                    with st.expander(f"{condition.title()}"):
                        st.markdown(f"**Overview:** {info['overview']}")
                        st.markdown(f"**Common Symptoms:** {', '.join(info['symptoms'][:5])}")
            else:
                st.info("No matching conditions found. Please provide more symptom details.")

# Treatment Plans
elif current_view == "Treatment Plans":
    st.subheader("Treatment Recommendations")
    condition = st.text_input("Enter a medical condition:")
    if st.button("Get Treatment Plan"):
        if condition:
            plan = generate_treatment_guidance(condition)
            st.markdown(plan)

# Health Analytics
elif current_view == "Health Analytics":
    st.subheader("Health Data Dashboard")
    data = get_sample_patient_data(30)
    st.line_chart(data.set_index("Date"))
    st.write("Recent readings:")
    st.dataframe(data.tail(7).style.format("{:.1f}"))
import streamlit as st
import plotly.express as px
from utils import get_sample_patient_data, get_patient_profile, generate_disease_prediction, generate_treatment_plan

st.set_page_config(page_title="HealthAI", page_icon="⚕️", layout="centered")
st.title("⚕️ HealthAI: Intelligent Healthcare Assistant")

menu = ["Patient Chat", "Disease Prediction", "Treatment Plans", "Health Analytics"]
choice = st.sidebar.radio("Choose a feature:", menu)

profile = get_patient_profile()
st.sidebar.markdown("### 🧑 Patient Profile")
st.sidebar.markdown(f"**Age:** {profile['age']}")
st.sidebar.markdown(f"**Gender:** {profile['gender']}")
st.sidebar.markdown(f"**Medical History:** {profile['medical_history']}")

# 1. Patient Chat (dummy logic)
if choice == "Patient Chat":
    st.subheader("💬 Patient Chat")
    query = st.text_input("Ask your health question:")
    if st.button("Get Answer"):
        if query:
            st.success("🤖 This is a general health response. Please consult a doctor for expert advice.")
        else:
            st.warning("Please enter a question.")

# 2. Disease Prediction
elif choice == "Disease Prediction":
    st.subheader("🤒 Disease Prediction")
    symptoms = st.text_area("Enter symptoms (e.g., fever, cough):")
    if st.button("Predict"):
        if symptoms:
            result = generate_disease_prediction(symptoms)
            st.success(result)
        else:
            st.warning("Enter symptoms to predict condition.")

# 3. Treatment Plans
elif choice == "Treatment Plans":
    st.subheader("💊 Treatment Plans")
    condition = st.text_input("Enter diagnosed condition (e.g., Diabetes):")
    if st.button("Get Plan"):
        if condition:
            plan = generate_treatment_plan(condition)
            st.success(plan)
        else:
            st.warning("Please enter a condition.")

# 4. Health Analytics
elif choice == "Health Analytics":
    st.subheader("📊 Health Analytics")
    df = get_sample_patient_data()
    metric = st.selectbox("Choose vital sign", ["Heart Rate", "Systolic BP", "Diastolic BP", "Blood Glucose"])
    fig = px.line(df, x="Date", y=metric, title=f"{metric} Over Time", markers=True)
    st.plotly_chart(fig, use_container_width=True)

    latest = df[metric].iloc[-1]
    delta = latest - df[metric].iloc[-2]
    st.metric(label=f"Latest {metric}", value=latest, delta=f"{delta:.1f}")
    st.markdown(f"**Average {metric}:** {df[metric].mean():.2f}")
    
