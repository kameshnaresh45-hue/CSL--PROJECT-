from flask import Flask, render_template, request
import google.generativeai as genai

# Configure API Key
genai.configure(api_key="AQ.Ab8RN6ISl3XJ8BPW7X_R3s3sGa-Cbu5kD-sWP9OW0Wvhgnbsjw")

app = Flask(__name__)

# Load Gemini Model
model = genai.GenerativeModel("gemini-1.5-flash")


@app.route("/", methods=["GET", "POST"])
def home():

    response_text = ""

    role = """
You are an AI Research Knowledge Assistant.
Explain AI, Machine Learning, and Deep Learning concepts.
Answer research-related questions clearly.
"""

    if request.method == "POST":

        prompt = request.form["prompt"]

        full_prompt = f"""
Role:
{role}

User Input:
{prompt}
"""

        response = model.generate_content(full_prompt)

        response_text = response.text

    return render_template(
        "index.html",
        message=response_text
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
