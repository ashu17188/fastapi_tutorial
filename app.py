#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 17:28:19 2021

@author: Ashutosh Shukla
"""

import uvicorn
from fastapi import FastAPI
from bank_notes import BankNotes
import numpy as np
import pandas as pd
import pickle


app = FastAPI()
pickle_in = open("banknote_classifier.pkl", "rb")
model = pickle.load(pickle_in)


@app.get('/')
def index():
    return {'message': 'Hello from bank note model'}


@app.get('/{name}')
def showName(name: str):
    return {'Welcome to model prediction': f'{name}'}


@app.post('/predict')
def predictBankNoteModel(data: BankNotes):
    data = data.dict()
    variance = data['variance']
    skewness = data['skewness']
    curtosis = data['curtosis']
    entropy = data['entropy']

    prediction = model.predict([[variance, skewness, curtosis, entropy]])
    if(prediction < 0.5):
        prediction = 'Fake Note'
    else:
        prediction = 'Its a Bank note'

    return {
        prediction
    }


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8080)
