from transformers import pipeline
import pandas as pd

# Load local model for Q&A (offline or internet-based, no key)
qa_model = pipeline("text-generation", model="gpt2")

def init_granite_model():
    def model(prompt):
        result = qa_model(prompt, max_length=100, num_return_sequences=1)
        return result[0]['generated_text']
    return model

def get_sample_patient_data():
    data = {
        "Name": ["Ravi", "Priya", "Amit", "Kiran", "Sneha"],
        "Age": [28, 34, 45, 23, 37],
        "Gender": ["Male", "Female", "Male", "Male", "Female"],
        "Diagnosis": ["Flu", "Diabetes", "Hypertension", "Anxiety", "Asthma"],
        "Last Visit": pd.to_datetime(["2024-12-12", "2025-02-10", "2025-04-05", "2025-06-01", "2025-05-22"])
    }
    return pd.DataFrame(data)

def get_patient_profile(name):
    df = get_sample_patient_data()
    profile = df[df["Name"].str.lower() == name.lower()]
    if profile.empty:
        return None
    return profile.to_dict(orient="records")[0]
