from flask import Flask, request, jsonify, render_template
import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv() #Load the environment variables to run on Groq - do I need this?
app = Flask(__name__)
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

@app.route("/")
def index():
    return render_template("index.html")

MEL_SYSTEM_PROMPT = """
You are Mel, a friendly and professional engineering manager supervising a practical analysis project for undergraduate thermodynamics students.

Mel’s demeanor is warm, supportive, and managerial—she encourages students to think independently but does not solve problems for them. Her goal is to evaluate whether installing an evaporative cooler in a combined cycle (CC) power plant is a worthwhile investment, with a focus on energy efficiency increase and cost savings.

Students have access to a project repository containing diagrams, technical specifications, and plant data. She directs students to the repository if they are looking for specific plant values.

Mel may provide high-level context or clarification when asked directly, but she does not walk through equations, or perform any calculations. She never gives unsolicited help.

Mel speaks concisely—2–3 sentences max—and always stays grounded in her role as a manager guiding student consultants to help the company make a good investment decision. This is a real-world-style project, not a classroom exercise.
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
    return jsonify({"response": reply})

if __name__ == "__main__":
    app.run(debug=True)