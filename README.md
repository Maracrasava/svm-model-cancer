# svm-model-cancer
Using support vector machines to determine whether person has a malignant or benign breast cancer.

Sklearn dataset has been used.

Useful resources:
https://www.analyticsvidhya.com/blog/2017/09/understaing-support-vector-machine-example-code/
https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html

SVC() has a lot parameters:
C- soft margin. How many data examples are acceptible inside a margin
Types of  kernel: kernel{‘linear’, ‘poly’, ‘rbf’, ‘sigmoid’, ‘precomputed’
Degree, gamma, etc

*Tip for splitting the data: You can use the parameter random_state to always get the same split.*
https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html
https://stackoverflow.com/questions/42191717/python-random-state-in-splitting-dataset

Note: When there are a lot features - Better to use SVM rather than KNN, since SVM handles huge dimension better.
