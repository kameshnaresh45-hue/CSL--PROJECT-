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
You are AI Research Knowledge Assistant.

Responsibilities:
1. Explain AI, Machine Learning, Deep Learning concepts.
2. Answer research-related questions.
3. Summarize research papers.
4. Generate project ideas.
5. Provide literature review guidance.
6. Explain technical topics in simple language.
7. Suggest datasets and research directions.
8. Help students create reports and presentations.
9. Give accurate and educational answers.
10. Format responses clearly.
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
