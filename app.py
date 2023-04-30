import openai
import gpt
import requests
import json
import time
api_key = ''
openai.api_key = api_key

def chatGPT(prompt):
    model_engine = "text-davinci-002" # Utilisez l'ID de modèle approprié pour GPT-3
    
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = response.choices[0].text.strip()
    return message

print("Bienvenue dans AUTO-GPT-3. ")
time.sleep(5.0)
id = 0 
urlDiscussion = 'http://127.0.0.1:8000/getDiscussion'
while True:
    questionA = json.loads(requests.get(urlDiscussion).text)[-1]
    answerA = chatGPT(questionA)
    requests.get('http://127.0.0.1:8000/addDiscussion/'+answerA)


    