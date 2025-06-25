import openai
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

class OpenAIModel:
    def generate_text(self, prompt: str) -> str:
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful and honest medical assistant."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=250,
                temperature=0.7
            )
            return response['choices'][0]['message']['content']
        except Exception as e:
            return f"⚠️ Error generating response: {e}"

def init_granite_model():
    return OpenAIModel()

def get_sample_patient_data():
    data = []
    start_date = datetime.now() - timedelta(days=30)
    for i in range(30):
        date = start_date + timedelta(days=i)
        heart_rate = int(np.random.normal(70, 5))
        systolic_bp = int(np.random.normal(120, 8))
        diastolic_bp = int(np.random.normal(80, 5))
        blood_glucose = int(np.random.normal(95, 10))
        data.append([date, heart_rate, systolic_bp, diastolic_bp, blood_glucose])
    df = pd.DataFrame(data, columns=['Date', 'Heart Rate', 'Systolic BP', 'Diastolic BP', 'Blood Glucose'])
    return df

def get_patient_profile():
    return {
        "age": 35,
        "gender": "Female",
        "medical_history": "No significant medical history, occasional seasonal allergies."
    }
