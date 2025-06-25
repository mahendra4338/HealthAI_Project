# utils.py (DUMMY VERSION)

# A simple dummy model class that just echoes back a canned response
class DummyModel:
    def generate_text(self, prompt: str) -> str:
        # You can customize responses here or make random ones
        return "⚕️ [Dummy Response] This is a placeholder answer for:\n\n" + prompt[:100] + "..."

def init_granite_model():
    """
    Dummy init function. Returns a DummyModel that simulates
    the Granite AI model for local testing without real API.
    """
    return DummyModel()

def get_sample_patient_data():
    """
    Generates and returns sample patient health metrics.
    """
    import pandas as pd
    import numpy as np
    from datetime import datetime, timedelta

    data = []
    start_date = datetime.now() - timedelta(days=30)
    for i in range(30):
        date = start_date + timedelta(days=i)
        # random but consistent-looking vitals
        heart_rate = int(np.random.normal(70, 5))
        systolic_bp = int(np.random.normal(120, 8))
        diastolic_bp = int(np.random.normal(80, 5))
        blood_glucose = int(np.random.normal(95, 10))
        data.append([date, heart_rate, systolic_bp, diastolic_bp, blood_glucose])

    df = pd.DataFrame(data, columns=['Date', 'Heart Rate', 'Systolic BP', 'Diastolic BP', 'Blood Glucose'])
    return df

def get_patient_profile():
    """
    Returns a sample patient profile.
    """
    return {
        "age": 35,
        "gender": "Female",
        "medical_history": "No significant medical history, occasional seasonal allergies."
    }
