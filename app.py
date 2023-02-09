import os

import openai
from flask import Flask, redirect, render_template, request, url_for
from logger import saveChatLog

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == 'POST':
        if len(request.form['question']) < 1:
            return render_template(
                'index.html', question="null", res="问题不能为空")
        question = request.form['question']
        print("======================================")
        print("接到请求:", question)
        res = get_completion(question)
        print("问题：\n", question)
        print("答案：\n", res)
        saveChatLog(question, res)

        return render_template('index.html', question=question, res=str(res))
    return render_template('index.html', question=0)    

def get_completion(question):
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=f"{question}\n",
            temperature=0.9,
            max_tokens=2048,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.6,
            stop=None
        )
    except Exception as e:

        print(e)
        return e
    return response["choices"][0].text
