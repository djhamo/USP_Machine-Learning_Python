# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 19:39:16 2019

@author: Tiago

-- Leave One Out --
Leave one out - MSE on test set: 15.465218791702433
Leave one out - MSE on train set: 19.220259837710353
"""

from sklearn.linear_model import Lasso

import sklearn as sk
import csv
import math
import numpy as np


lines = csv.reader(open("reg01.csv", "r"),delimiter=',')
header = next(lines)
dataset = list(lines)

X_data_temp = [[eval(x) for x in t] for t in dataset]
#print(X_data_temp)
X_data = [X_data_temp[i][:10] for i in range(len(X_data_temp))] 
#print(X_data)
y_data = [eval(t[-1]) for t in dataset]
#print(y_data)
 

print('-- Leave One Out --')
MSEtrainset_accuracy=0
MSEtestset_accuracy=0
for i in range(len(dataset)):
    X_test = np.array(X_data[i]).reshape(-1,1).T
    y_test = np.array(y_data[i]).reshape(-1,1)
    X_train = np.array(X_data[:i]+X_data[i+1:])
    y_train = np.array(y_data[:i]+y_data[i+1:]).reshape(-1,1)
    
    las = Lasso(alpha=1)
    las.fit(X_train, y_train)
    
    MSEtestset_accuracy += (math.sqrt(sk.metrics.mean_squared_error(y_test, las.predict(X_test))))
    MSEtrainset_accuracy += (math.sqrt(sk.metrics.mean_squared_error(y_train, las.predict(X_train))))
    

print(('Leave one out - MSE on test set: {0}').format(np.mean(MSEtestset_accuracy)))
print(('Leave one out - MSE on train set: {0}').format(np.mean(MSEtrainset_accuracy)))