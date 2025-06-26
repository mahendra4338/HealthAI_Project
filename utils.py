import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def get_sample_patient_data():
    data = []
    start = datetime.now() - timedelta(days=30)
    for i in range(30):
        date = start + timedelta(days=i)
        data.append([
            date,
            int(np.random.normal(72, 4)),     # Heart Rate
            int(np.random.normal(120, 6)),    # Systolic
            int(np.random.normal(80, 5)),     # Diastolic
            int(np.random.normal(95, 10))     # Glucose
        ])
    df = pd.DataFrame(data, columns=["Date", "Heart Rate", "Systolic BP", "Diastolic BP", "Blood Glucose"])
    return df

def get_patient_profile():
    return {
        "age": 35,
        "gender": "Female",
        "medical_history": "No significant medical history, occasional seasonal allergies."
    }

def generate_disease_prediction(symptoms):
    s = symptoms.lower()
    if "fever" in s and "cough" in s:
        return "🦠 Possible: Flu, Viral Fever, COVID-19\n💡 Stay hydrated and monitor symptoms."
    elif "headache" in s:
        return "🧠 Possible: Migraine, Tension Headache\n💡 Take rest and avoid screen time."
    elif "fatigue" in s:
        return "💤 Possible: Anemia, Thyroid Issue\n💡 Eat healthy and consult if persists."
    else:
        return "❓ No clear match found. Try more specific symptoms."

def generate_treatment_plan(condition):
    c = condition.lower()
    if "diabetes" in c:
        return "🩺 Plan:\n- Metformin 500mg twice daily\n- Low sugar diet\n- 30 min walk\n- Glucose test weekly"
    elif "hypertension" in c:
        return "🩺 Plan:\n- Amlodipine 5mg daily\n- Reduce salt\n- Check BP twice a week\n- Yoga and exercise"
    elif "asthma" in c:
        return "🩺 Plan:\n- Inhaler (Salbutamol)\n- Avoid cold/dust\n- Monitor with peak flow meter"
    else:
        return "⚠️ No specific plan found. Consult a doctor."
 --- Project Links (For Reference) ---
App Link: https://healthaiproject-9zncftohtgbtxnwcvrkdss.streamlit.app
GitHub: https://github.com/mahendra4338/HealthAI_Project

