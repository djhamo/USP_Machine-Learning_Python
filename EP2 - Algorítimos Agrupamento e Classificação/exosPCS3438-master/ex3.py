from sklearn.linear_model import Lasso

import sklearn as sk
import csv
import random
import math
import numpy as np


lines = csv.reader(open("reg01.csv", "r"),delimiter=',')
header = next(lines)
dataset = list(lines)

X_data = [[eval(x) for x in t] for t in dataset]
y_data = [eval(t[-1]) for t in dataset]


print('-- Leave One Out --')
MSEtrainset_accuracy=0
MSEtestset_accuracy=0
for i in range(len(dataset)):
    X_test = np.array(X_data[i]).reshape(-1,1).T
    y_test = np.array(y_data[i]).reshape(-1,1)
    X_train = np.array(X_data[:i]+X_data[i+1:])
    y_train = np.array(y_data[:i]+y_data[i+1:]).reshape(-1,1)

    las = Lasso(alpha=1, normalize=True)
    las.fit(X_train, y_train)

    MSEtestset_accuracy += sk.metrics.mean_squared_error(y_test, las.predict(X_test)) /len(dataset)
    MSEtrainset_accuracy += sk.metrics.mean_squared_error(y_train, las.predict(X_train)) /len(dataset)

print(('Leave one out - MSE on train set: {0}').format(MSEtrainset_accuracy))
print(('Leave one out - MSE on test set: {0}').format(MSEtestset_accuracy))
