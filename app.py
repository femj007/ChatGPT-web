import os

import openai
from flask import Flask, redirect, render_template, request, url_for
from logger import saveChatLog
from ChatBot import Chatbot

app = Flask(__name__)

API_KEY = os.getenv("OPENAI_API_KEY")

chatbot = Chatbot(
    api_key=API_KEY
)

@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == 'POST':
        if len(request.form['question']) < 1:
            return render_template(
                'index.html', question="null", res="问题不能为空")
        prev_text = ""
        question = request.form['question']
        print("======================================")
        print("Human:", question)
        res = chatbot.ask(question)

        print("Question: \n", question)
        print("Answer: \n", res)
        saveChatLog(question, res)

        return render_template('index.html', question=question, res=str(res))
    return render_template('index.html', question=0)    

# TODO: a function to chat
@app.route("/chat", methods=("GET", "POST"))
def chat():
    if request.method == 'POST':
        try:
            question = request.form['question']
            prev_text = ""
            print("======================================")
            print("Human:", question)
            res = ''
            for data in chatbot.ask(question):
                message = data["message"][len(prev_text) :]
                res += message
                print(message, end="", flush=True)
                prev_text = data["message"]
            
            saveChatLog(question, res)
            return jsonify({"response": res}), 200


        except Exception as e:
            print(e)
            return e

if __name__ == "__main__":
    app.run(host='0.0.0.0')