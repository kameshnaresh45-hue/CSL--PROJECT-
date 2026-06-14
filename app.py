from flask import Flask, render_template, request
from openai import OpenAI

app = Flask(__name__)

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="sk-or-v1-9a039ba45c13eca464dff25ccdf7a790245d143b2d9e8e26b9807>"
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
            model="deepseek/deepseek-r1",
            messages=[
                {
                    "role": "system",
                    "content": role
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        response_text = response.choices[0].message.content

    return render_template(
        "index.html",
        message=response_text
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
