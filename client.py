from revChatGPT.V1 import Chatbot
import os

chatbot = Chatbot(config={
  "email": os.getenv("OPENAI_EMAIL"),
  "password": os.getenv("OPENAI_PASSWORD")
})

print("Chatbot: ")
prev_text = ""
for data in chatbot.ask(
    "Hello world",
):
    message = data["message"][len(prev_text) :]
    print(message, end="", flush=True)
    prev_text = data["message"]
print()