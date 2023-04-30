from typing import Union
from fastapi import FastAPI
import json
from fastapi.middleware.cors import CORSMiddleware
import requests
from datetime import datetime

app = FastAPI()
origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/addDiscussion/{word}')
async def addDiscussion(word : str):
    with open ('discussion.txt', 'a') as file:  
        file.write(str(datetime.now())+' : '+word)
        file.write('\n')
@app.get('/getDiscussion')
async def getDiscussion():
    with open('discussion.txt') as file:
        w = file.read().split('\n')
        return w 
        
  