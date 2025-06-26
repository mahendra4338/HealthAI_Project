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
    # --- Project Links ---
st.markdown("---")
st.markdown("### 🔗 Project Links")
st.markdown("[🌐 Open App in Browser](https://healthaiproject-9zncftohtgbtxnwcvrkdss.streamlit.app)", unsafe_allow_html=True)
st.markdown("[💻 View on GitHub](https://github.com/mahendra4338/HealthAI_Project)", unsafe_allow_html=True)

