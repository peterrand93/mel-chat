# app.py
from flask import Flask, request, jsonify, render_template
import os
from groq import Groq

app = Flask(__name__, template_folder="templates")

@app.get("/")
def index():
    return render_template("index.html")

@app.get("/health")
def health():
    return "ok", 200

MEL_SYSTEM_PROMPT = """
You are Mel, a friendly and professional engineering manager supervising a practical analysis project for undergraduate thermodynamics students.
Mel’s demeanor is warm, supportive, and managerial—she encourages students to think independently but does not solve problems for them...
"""

def get_groq_client():
    key = os.getenv("GROQ_API_KEY")
    if not key:
        # Fail inside a request, not on import
        raise RuntimeError("GROQ_API_KEY not set")
    return Groq(api_key=key)

@app.post("/mel")
def mel():
    user_message = request.json.get("message", "")
    client = get_groq_client()

    resp = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": MEL_SYSTEM_PROMPT},
            {"role": "user", "content": user_message},
        ],
        temperature=0.7,
        max_tokens=1000,  # keep responses snappy; adjust if needed
    )
    reply = resp.choices[0].message.content.strip()
    return jsonify({"response": reply})
