from sklearn import metrics
import numpy as np
import csv
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
clf=RandomForestClassifier(n_estimators=100)

data=np.loadtxt(open("transport_newdata.csv", "r"), delimiter=",")
questions=np.loadtxt(open("transport_quest.csv","r"), delimiter=",")

X = data[:,0:4]
y = data[:,4]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.70, random_state=0)
clf.fit(X_train, y_train) 
z=list(clf.predict(X_test))
print(metrics.classification_report(y_test, z))

clf.fit(X, y) 
out = open('transport_output_rforest.txt', 'w')
z=list(clf.predict(questions))

for i in range(len(z)):
    out.write(str(int(z[i])) + '\n') 
out.close()