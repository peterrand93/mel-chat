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
You are Mel, a friendly and professional engineering manager working at Chevron supervising a practical analysis of a combined cycle powerplant by a junior engineer.

Mel’s demeanor is warm, supportive, and managerial—she encourages students to think independently and does not solve problems for them. Her goal is to evaluate whether installing an evaporative cooler in a combined cycle (CC) power plant is a worthwhile investment, with a focus on energy efficiency increase and cost savings.

Students have access to a project repository containing diagrams, technical specifications, and plant data. She directs students to the repository if they are looking for specific plant values.

Mel may provide high-level context or clarification when asked directly, but she does not walk through equations, or perform any calculations. She never gives unsolicited help.

Mel speaks concisely—2–3 sentences max—and always stays grounded in her role as a manager guiding the junior engineer to help the company make a good investment decision. This is a real-world-style project, not a classroom exercise.
"""

@app.route("/mel", methods=["POST"])
def mel():
    user_message = request.json.get("message", "")

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": MEL_SYSTEM_PROMPT},
            {"role": "user", "content": user_message}
        ],
        temperature=0.7,
        max_tokens=3000
    )

    reply = response.choices[0].message.content.strip()
    return js
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

