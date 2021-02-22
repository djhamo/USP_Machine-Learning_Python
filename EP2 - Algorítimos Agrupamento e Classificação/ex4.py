# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 09:52:36 2019

@author: Tiago

Mean Absolute Error: 51.02853074153567
Mean Squared Error: 4434.737895080578
Root Mean Squared Error: 66.59382775513492
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv('reg02.csv')

#print(dataset.head())
#print(dataset.describe())

X = dataset.drop('target', axis=1)
y = dataset['target']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor()
regressor.fit(X_train, y_train)

y_pred = regressor.predict(X_test)
y_pred_train = regressor.predict(X_train)

df=pd.DataFrame({'Actual':y_test, 'Predicted':y_pred})
print(df)

from sklearn import metrics
print('Teste')
print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

print('Treino')
print('Mean Absolute Error:', metrics.mean_absolute_error(y_train, y_pred_train))
print('Mean Squared Error:', metrics.mean_squared_error(y_train, y_pred_train))
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_train, y_pred_train)))