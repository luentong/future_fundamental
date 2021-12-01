import csv
with open('last five year.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    X = []
    y = []
    index = 0
    for row in spamreader:

        if index == 0:
            index += 1
            continue

        subx = row[0].split(";")[1]
        a = float(subx.strip('%')) / 100
        y.append(float(subx.strip('%')) / 100)
        suby = row[0].split(";")[2]
        X.append(float(suby.strip('%'))/100)
print(X)
print(y)
print(len(X))
print(len(y))

import numpy as np
from sklearn.linear_model import LinearRegression
X = np.array(X).reshape(-1,1)
y = np.array(y).reshape(-1,1)
reg = LinearRegression().fit(X, y)
print(reg.score(X, y))
print(reg.coef_)
print(reg.intercept_)