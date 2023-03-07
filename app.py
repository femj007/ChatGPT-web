import os

import openai
from flask import Flask, redirect, render_template, request, url_for, jsonify 
from logger import saveChatLog
from ChatBot import Chatbot
import requests

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
        print("Answer: \n", res)
        saveChatLog(question, res)

        return render_template('index.html', question=question, res=str(res))
    return render_template('index.html', question=0)    

# TODO: a function to chat
@app.route("/chat", methods=["POST"])
def chat():
    if request.method == 'POST':
        try:
            question = request.form['question']
            print(question)
            prev_text = ""
            print("======================================")
            print("Human:", question)
            res = chatbot.ask(question)

            # Get response
            session = requests.Session()
            response = session.post(
                "https://api.openai.com/v1/chat/completions",
                headers={"Authorization": f"Bearer {API_KEY}"},
                json=question,
                stream=True,
            )
            print(response)
            print("Answer: \n", res)
            saveChatLog(question, res)
            return jsonify({"response": res}), 200


        except Exception as e:
            print(e)
            return jsonify({"response": str(e)}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0')