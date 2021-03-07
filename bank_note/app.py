from fastapi import APIRouter, Depends, Request
from bank_note.notes import BankNotes
import numpy as np
import pandas as pd
import pickle

api = APIRouter()
pickle_in = open("./bank_note/banknote_classifier.pkl", "rb")
model = pickle.load(pickle_in)

@api.post('/predict')
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

