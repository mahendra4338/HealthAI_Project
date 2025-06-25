import streamlit as st
import pandas as pd
import plotly.express as px
from utils import init_granite_model, get_sample_patient_data, get_patient_profile
import datetime

# --- Streamlit Configuration ---
st.set_page_config(
    page_title="HealthAI: Intelligent Healthcare Assistant",
    page_icon="⚕️",
    layout="wide"
)

# --- Initialize OpenAI Model ---
try:
    granite_model = init_granite_model()
except ValueError as e:
    st.error(f"Configuration Error: {e}. Please ensure your .env file is correctly set up.")
    granite_model = None

# --- UI Title and Sidebar ---
st.title("⚕️ HealthAI: Intelligent Healthcare Assistant")
st.sidebar.title("Navigation")

feature_selection = st.sidebar.radio(
    "Choose a feature:",
    ("Patient Chat", "Disease Prediction", "Treatment Plans", "Health Analytics")
)

# --- Patient Chat Feature ---
if feature_selection == "Patient Chat":
    st.subheader("💬 Chat with HealthAI Assistant")
    user_input = st.text_input("Describe your symptoms or ask a health question:")
    if st.button("Get Response"):
        if user_input.strip() != "":
            with st.spinner("Thinking..."):
                if granite_model:
                    response = granite_model(user_input)
                    st.success("Assistant Response:")
                    st.write(response)
                else:
                    st.error("Model not initialized.")

# --- Disease Prediction (Placeholder for now) ---
elif feature_selection == "Disease Prediction":
    st.subheader("🧬 Disease Prediction")
    st.info("This feature is under development. Future updates will include predictive models based on symptoms and patient history.")

# --- Treatment Plans (Based on patient name) ---
elif feature_selection == "Treatment Plans":
    st.subheader("📋 Treatment Plans")
    name = st.text_input("Enter patient name (e.g., Ravi):")
    if st.button("Get Profile"):
        profile = get_patient_profile(name)
        if profile:
            st.write("### Patient Profile")
            st.json(profile)
            st.success("Treatment recommendation (sample):")
            st.write(f"Based on {profile['Diagnosis']}, regular checkups and medication are advised. Please consult a certified doctor.")
        else:
            st.warning("No patient found with that name.")

# --- Health Analytics ---
elif feature_selection == "Health Analytics":
    st.subheader("📊 Health Analytics Dashboard")
    df = get_sample_patient_data()
    st.dataframe(df)

    st.write("### Diagnosis Distribution")
    fig1 = px.histogram(df, x="Diagnosis", color="Gender", barmode="group", title="Diagnosis by Gender")
    st.plotly_chart(fig1, use_container_width=True)

    st.write("### Last Visit Timeline")
    fig2 = px.bar(df, x="Name", y="Last Visit", color="Diagnosis", title="Last Visit per Patient")
    st.plotly_chart(fig2, use_container_width=True)
