from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.dummy import DummyClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix

X, y = load_diabetes(return_X_y = True)
y = (y > 140).astype(int)
X_train, X_test, y_train, y_test = train_test_split\
    (X, y, test_size = 0.2, random_state = 42)

model = LogisticRegression()
model.fit(X_train, y_train)

pred = model.predict(X_test)

print("정확도=", accuracy_score(y_test, pred))
print("정밀도=", precision_score(y_test, pred))

base = DummyClassifier(strategy="most_frequent")
base.fit(X_train, y_train)
base_pred = base.predict(X_test)

print("재현율=", recall_score (y_test, pred))
print("실제 1인 찾아낸 비율=", confusion_matrix(y_test, pred))


print("기준 모델 정확도 =", accuracy_score(y_test, base_pred))