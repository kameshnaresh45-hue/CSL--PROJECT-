from flask import Flask, render_template, request
from openai import OpenAI

app = Flask(__name__)

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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"
)
@app.route("/", methods=["GET", "POST"])
def home():

    response_text = ""

    role = """
You are AI Research Knowledge Assistant.,Explain AI, Machine Learning, Deep Learning concepts,Answer research-related questions.
"""

    if request.method == "POST":

        prompt = request.form["prompt"]
        response = client.chat.completions.create(
    model="~openai/gpt-latest",
    messages=[
        {"role": "user", "content":f" your role :{role},user input : {prompt}" }
    ], max_tokens=100
)       

        response_text = response.choices[0].message.content

    return render_template(
        "index.html",
        message=response_text
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
