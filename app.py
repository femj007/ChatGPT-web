import os

import openai
from flask import Flask, redirect, render_template, request, url_for
from logger import saveChatLog
from revChatGPT.V1 import Chatbot

app = Flask(__name__)

my_email = os.getenv("OPENAI_EMAIL")
my_password = os.getenv("OPENAI_PASSWORD")
chatbot = Chatbot(config={
  "email": my_email,
  "password": my_password,
  "paid": True # Change to False if the account is not plus
})

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
        res = ''
        for data in chatbot.ask(question):
            message = data["message"][len(prev_text) :]
            res += message
            print(message, end="", flush=True)
            prev_text = data["message"]
        
        print("Question: \n", question)
        print("Answer: \n", res)
        saveChatLog(question, res)

        return render_template('index.html', question=question, res=str(res))
    return render_template('index.html', question=0)    

# TODO: a function to chat
@app.route("/chat", methods=("POST"))
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

