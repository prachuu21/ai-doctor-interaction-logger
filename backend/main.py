from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Interaction(BaseModel):
    doctor_name: str
    discussion: str

@app.post("/log")
def log_interaction(data: Interaction):
    return {
        "message": "Interaction logged",
        "doctor": data.doctor_name,
        "summary": f"Discussion with {data.doctor_name}: {data.discussion}"
    }

from groq import Groq

client = Groq(api_key="YOUR_GROQ_API_KEY")

def generate_summary(text):

    response = client.chat.completions.create(
        model="gemma2-9b-it",
        messages=[
            {"role": "system", "content": "You are a medical CRM assistant."},
            {"role": "user", "content": f"Summarize this doctor interaction: {text}"}
        ]
    )

    return response.choices[0].message.content

@app.post("/log")
def log_interaction(data: Interaction):

    summary = generate_summary(data.discussion)

    return {
        "doctor": data.doctor_name,
        "discussion": data.discussion,
        "ai_summary": summary
    }