from sklearn.linear_model import LogisticRegression
from sklearn.dummy import DummyClassifier
from sklearn.metrics import (accuracy_score, precision_score, recall_score, confusion_matrix)

y_train = (y_train > 140).astype(int)
y_test = (y_test > 140).astype(int)

clf = LogisticRegression(max_iter = 1000)
clf.fit(y_train, y_test)

pred = clf.predict(y_test)

print("정확도=%.4f"% accuracy_score(y_train_c, pred) )
