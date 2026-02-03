import os
from groq import Groq

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def call_groq(messages, temperature=0.3):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages,
        temperature=temperature,
        max_tokens=4000
    )
    return response.choices[0].message.content
