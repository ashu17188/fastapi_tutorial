#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 17:16:08 2021

@author: administrator
"""
import numpy as np
import pandas as pd

df = pd.read_csv('BankNote_Authentication.csv')
#print(df)

X = df.iloc[:,:-1]
y = df.iloc[:, -1]

from sklearn import model_selection

X_train,X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.24, random_state=0)

from sklearn import ensemble
model = ensemble.RandomForestClassifier()
model.fit(X_train,y_train)

y_pred = model.predict(X_test)

from sklearn import metrics
score = metrics.accuracy_score(y_test, y_pred)

import pickle
picker_out = open("banknote_classifier.pkl","wb")
pickle.dump(model, picker_out)
picker_out.close()

print(model.predict([[2,3,4,1]]))