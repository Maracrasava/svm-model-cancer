import sklearn
from sklearn import svm
from sklearn import datasets
from sklearn import metrics

cancer = datasets.load_breast_cancer()

# Features value
X = cancer.data
# Malignant or benign(0/1)
y = cancer.target

X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.15, random_state=42)

# Parameters: margin, kernel type, etc
mdl = svm.SVC()
mdl.fit(X_train, y_train)
prediction = mdl.predict(X_test)
#Order inside brackets is no matter
acc = metrics.accuracy_score(y_test, prediction)
print(acc)

