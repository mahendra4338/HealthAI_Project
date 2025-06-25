import openai

openai.api_key = "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"

def init_granite_model():
    def model(prompt):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful healthcare assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message['content']
    return model

def get_sample_patient_data():
    import pandas as pd
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
