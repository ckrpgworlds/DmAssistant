from flask import Flask, request, render_template
import openai
import os
from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__)

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        prompt = request.form["prompt"]

        # Send prompt to OpenAI using new SDK format
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )
        result = response.choices[0].message.content

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
