import datetime

#save chat log 
def saveChatLog(question, answer):
    date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open('log.txt', 'a', encoding="utf-8") as f:
        f.write(f'[{date}] Question: {question} Answer: {answer}\n')
        
    