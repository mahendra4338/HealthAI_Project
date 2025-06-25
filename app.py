import streamlit as st
import pandas as pd
from utils import init_granite_model, get_sample_patient_data, get_patient_profile
import datetime
import plotly.express as px

st.set_page_config(
    page_title="HealthAI: Intelligent Healthcare Assistant",
    page_icon="⚕️",
    layout="wide"
)

try:
    granite_model = init_granite_model()
except Exception as e:
    st.error(f"Model initialization failed: {e}")
    granite_model = None

st.title("⚕️ HealthAI: Intelligent Healthcare Assistant")
st.sidebar.title("Navigation")

feature_selection = st.sidebar.radio(
    "Choose a feature:",
    ("Patient Chat", "Disease Prediction", "Treatment Plans", "Health Analytics")
)

if feature_selection == "Patient Chat":
    st.subheader("💬 Ask Health Questions")
    user_input = st.text_input("Enter your question:")
    if st.button("Get Answer"):
        if granite_model and user_input:
            with st.spinner("Generating response..."):
                response = granite_model(user_input)
                st.success(response)
        else:
            st.warning("Model not initialized or input is empty.")

elif feature_selection == "Health Analytics":
    st.subheader("📊 Patient Health Data")
    df = get_sample_patient_data()
    st.dataframe(df)

    fig = px.histogram(df, x="Diagnosis", color="Gender", barmode="group", title="Patient Diagnoses by Gender")
    st.plotly_chart(fig)

    selected_name = st.selectbox("Select a patient to view profile:", df["Name"].unique())
    profile = get_patient_profile(selected_name)
    if profile:
        st.write("### Patient Profile")
        st.json(profile)
    else:
        st.warning("Profile not found.")

else:
    st.subheader("🚧 This feature is under construction.")
