from flask import Flask, request, jsonify, render_template
import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/mel", methods=["POST"])
def mel():
    user_message = request.json.get("message", "")

    response = client.chat.completions.create(
        model="mistral-saba-24b",
        messages=[
            {"role": "system", "content": "You are Mel, a no-nonsense engineering manager helping undergrads with a thermodynamics power plant design project. Be clear, helpful, and a little tough."},
            {"role": "user", "content": user_message}
        ],
        temperature=0.7,
        max_tokens=300
    )

    reply = response.choices[0].message.content.strip()
    return jsonify({"response": reply})