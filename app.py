from flask import Flask, render_template, request
from google import genai
app = Flask(__name__)
client = genai.Client(api_key="AQ.Ab8RN6LKqXfyQ4ypOooSOOvg8x8rHBYvRcOl0ITa-tK63y-EKg")

@app.route("/", methods=["GET", "POST"])
def home():

    response_text = ""

    role = """
You are AI Research Knowledge Assistant.,Explain AI, Machine Learning, Deep Learning concepts,Answer research-related questions.
"""

    if request.method == "POST":

        prompt = request.form["prompt"]
        response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=f" your role :{role},user input : {prompt}"
)
     

        response_text = response.text

    return render_template(
        "index.html",
        message=response_text
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
