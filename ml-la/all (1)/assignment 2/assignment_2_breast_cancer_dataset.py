# -*- coding: utf-8 -*-
"""Assignment-2 Breast Cancer dataset.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1t6NYfZYxHAKKhxulHCcCYH02vJv1Kdav

# 1. Import required modules
"""

import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import seaborn as sns
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import RandomForestClassifier



"""# 2. Load Dataset"""

b_cancer = datasets.load_breast_cancer() 
# it's source is same as : https://archive.ics.uci.edu/ml/datasets/wine

dir(b_cancer)

b_cancer.data

print(b_cancer.feature_names)
print(b_cancer.target_names)
print(b_cancer.target)

df = pd.DataFrame(data=b_cancer.data, columns=b_cancer.feature_names)
df.head()

df["target"] = b_cancer.target
df.head()

df.target.value_counts()

len(df)

X = df.drop(["target"], axis="columns")
y = df.target
print(X.head())
print(y.head())

"""# 3. SVC Classfier

## Linear SVC Classifier
"""

linear_SVC_classifier = SVC(kernel='linear')
linear_SVC_classifier



"""### train size : test size = 70% : 30%

"""

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)    # 70% training data, 30% testing data

print(len(X_train))
print(len(y_test))

linear_SVC_classifier.fit(X_train, y_train)

y_pred = linear_SVC_classifier.predict(X_test)
print(f"Accuracy: {100 * accuracy_score(y_test,y_pred)}%\n")
cf_matrix = confusion_matrix(y_test,y_pred)
print("Confusion Matrix:\n")
print(cf_matrix)
print("\nClassification Report:\n")
print(classification_report(y_test,y_pred))

sns.heatmap(cf_matrix, annot=True)

"""### train size : test size = 60% : 40%"""

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=0)    # 60% training data, 40% testing data

print(len(X_train))
print(len(y_test))

linear_SVC_classifier.fit(X_train, y_train)

y_pred = linear_SVC_classifier.predict(X_test)
print(f"Accuracy: {100 * accuracy_score(y_test,y_pred)}%\n")
cf_matrix = confusion_matrix(y_test,y_pred)
print("Confusion Matrix:")
print(cf_matrix)
print("\nClassification Report:\n")
print(classification_report(y_test,y_pred))

sns.heatmap(cf_matrix, annot=True)

"""### train size : test size = 50% : 50%"""

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=0)    # 50% training data, 50% testing data

print(len(X_train))
print(len(y_test))

linear_SVC_classifier.fit(X_train, y_train)

y_pred = linear_SVC_classifier.predict(X_test)
print(f"Accuracy: {100 * accuracy_score(y_test,y_pred)}%\n")
cf_matrix = confusion_matrix(y_test,y_pred)
print("Confusion Matrix:")
print(cf_matrix)
print("\nClassification Report:\n")
print(classification_report(y_test,y_pred))

sns.heatmap(cf_matrix, annot=True)

"""### train size : test size = 40% : 60%"""

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.6, random_state=0)

print(len(X_train))
print(len(y_test))

linear_SVC_classifier.fit(X_train, y_train)

y_pred = linear_SVC_classifier.predict(X_test)
print(f"Accuracy: {100 * accuracy_score(y_test,y_pred)}%\n")
cf_matrix = confusion_matrix(y_test,y_pred)
print("Confusion Matrix:\n")
print(cf_matrix)
print("\nClassification Report:\n")
print(classification_report(y_test,y_pred))

sns.heatmap(cf_matrix, annot=True)

"""### train size : test size = 30% : 70%"""

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.7, random_state=0)

print(len(X_train))
print(len(y_test))

linear_SVC_classifier.fit(X_train, y_train)

y_pred = linear_SVC_classifier.predict(X_test)
print(f"Accuracy: {100 * accuracy_score(y_test,y_pred)}%\n")
cf_matrix = confusion_matrix(y_test,y_pred)
print("Confusion Matrix:\n")
print(cf_matrix)
print("\nClassification Report:\n")
print(classification_report(y_test,y_pred))

sns.heatmap(cf_matrix, annot=True)

"""## Polynomial SVC Classifier"""

poly_SVC_classifier = SVC(kernel='poly')
poly_SVC_classifier

"""### train size : test size = 70% : 30%"""

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

print(len(X_train))
print(len(y_test))

poly_SVC_classifier.fit(X_train, y_train)

y_pred = poly_SVC_classifier.predict(X_test)
print(f"Accuracy: {100 * accuracy_score(y_test,y_pred)}%\n")
cf_matrix = confusion_matrix(y_test,y_pred)
print("Confusion Matrix:\n", cf_matrix)
print("\nClassification Report:\n")
print(classification_report(y_test,y_pred))

sns.heatmap(cf_matrix, annot=True)

"""### train size : test size = 60% : 40%


"""

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=0)

print(len(X_train))
print(len(y_test))

poly_SVC_classifier.fit(X_train, y_train)

y_pred = poly_SVC_classifier.predict(X_test)
print(f"Accuracy: {100 * accuracy_score(y_test,y_pred)}%\n")
cf_matrix = confusion_matrix(y_test,y_pred)
print("Confusion Matrix:\n", cf_matrix)
print("\nClassification Report:\n")
print(classification_report(y_test,y_pred))

sns.heatmap(cf_matrix, annot=True)

"""### train size : test size = 50% : 50%

"""

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=0)

print(len(X_train))
print(len(y_test))

poly_SVC_classifier.fit(X_train, y_train)

y_pred = poly_SVC_classifier.predict(X_test)
print(f"Accuracy: {100 * accuracy_score(y_test,y_pred)}%\n")
cf_matrix = confusion_matrix(y_test,y_pred)
print("Confusion Matrix:\n", cf_matrix)
print("\nClassification Report:\n")
print(classification_report(y_test,y_pred))

sns.heatmap(cf_matrix, annot=True)

"""### train size : test size = 40% : 60%"""

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.6, random_state=0)

print(len(X_train))
print(len(y_test))

poly_SVC_classifier.fit(X_train, y_train)

y_pred = poly_SVC_classifier.predict(X_test)
print(f"Accuracy: {100 * accuracy_score(y_test,y_pred)}%\n")
cf_matrix = confusion_matrix(y_test,y_pred)
print("Confusion Matrix:\n", cf_matrix)
print("\nClassification Report:\n")
print(classification_report(y_test,y_pred))

sns.heatmap(cf_matrix, annot=True)

"""### train size : test size = 30% : 70%"""

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.7, random_state=0)

print(len(X_train))
print(len(y_test))

poly_SVC_classifier.fit(X_train, y_train)

y_pred = poly_SVC_classifier.predict(X_test)
print(f"Accuracy: {100 * accuracy_score(y_test,y_pred)}%\n")
cf_matrix = confusion_matrix(y_test,y_pred)
print("Confusion Matrix:\n", cf_matrix)
print("\nClassification Report:\n")
print(classification_report(y_test,y_pred))

sns.heatmap(cf_matrix, annot=True)

"""## Gaussain SVC Classifier"""

gaussain_SVC_classifier = SVC(kernel='rbf')
gaussain_SVC_classifier

"""### train size : test size = 70% : 30%"""

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

print(len(X_train))
print(len(y_test))

gaussain_SVC_classifier.fit(X_train, y_train)

y_pred = gaussain_SVC_classifier.predict(X_test)
print(f"Accuracy: {100 * accuracy_score(y_test,y_pred)}%\n")
cf_matrix = confusion_matrix(y_test,y_pred)
print("Confusion Matrix:\n", cf_matrix)
print("\nClassification Report:\n")
print(classification_report(y_test,y_pred))

sns.heatmap(cf_matrix, annot=True)

"""### train size : test size = 60% : 40%


"""

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=0)

print(len(X_train))
print(len(y_test))

gaussain_SVC_classifier.fit(X_train, y_train)

y_pred = gaussain_SVC_classifier.predict(X_test)
print(f"Accuracy: {100 * accuracy_score(y_test,y_pred)}%\n")
cf_matrix = confusion_matrix(y_test,y_pred)
print("Confusion Matrix:\n", cf_matrix)
print("\nClassification Report:\n")
print(classification_report(y_test,y_pred))

sns.heatmap(cf_matrix, annot=True)

"""### train size : test size = 50% : 50%"""

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=0)

print(len(X_train))
print(len(y_test))

gaussain_SVC_classifier.fit(X_train, y_train)

y_pred = gaussain_SVC_classifier.predict(X_test)
print(f"Accuracy: {100 * accuracy_score(y_test,y_pred)}%\n")
cf_matrix = confusion_matrix(y_test,y_pred)
print("Confusion Matrix:\n", cf_matrix)
print("\nClassification Report:\n")
print(classification_report(y_test,y_pred))

sns.heatmap(cf_matrix, annot=True)

"""### train size : test size = 40% : 60%"""

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.6, random_state=0)

print(len(X_train))
print(len(y_test))

gaussain_SVC_classifier.fit(X_train, y_train)

y_pred = gaussain_SVC_classifier.predict(X_test)
print(f"Accuracy: {100 * accuracy_score(y_test,y_pred)}%\n")
cf_matrix = confusion_matrix(y_test,y_pred)
print("Confusion Matrix:\n", cf_matrix)
print("\nClassification Report:\n")
print(classification_report(y_test,y_pred))

sns.heatmap(cf_matrix, annot=True)

"""### train size : test size = 30% : 70%"""





X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.7, random_state=0)

print(len(X_train))
print(len(y_test))

gaussain_SVC_classifier.fit(X_train, y_train)

y_pred = gaussain_SVC_classifier.predict(X_test)
print(f"Accuracy: {100 * accuracy_score(y_test,y_pred)}%\n")
cf_matrix = confusion_matrix(y_test,y_pred)
print("Confusion Matrix:\n", cf_matrix)
print("\nClassification Report:\n")
print(classification_report(y_test,y_pred))

sns.heatmap(cf_matrix, annot=True)

"""## Sigmoid SVC Classifier"""

sigmoid_SVC_classifier = SVC(kernel='sigmoid', C=0.9)
sigmoid_SVC_classifier

"""### train size : test size = 70% : 30%"""

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

print(len(X_train))
print(len(y_test))

sigmoid_SVC_classifier.fit(X_train, y_train)

y_pred = sigmoid_SVC_classifier.predict(X_test)
print(f"Accuracy: {100 * accuracy_score(y_test,y_pred)}%\n")
cf_matrix = confusion_matrix(y_test,y_pred)
print("Confusion Matrix:\n", cf_matrix)
print("\nClassification Report:\n")
print(classification_report(y_test,y_pred))

from sklearn.model_selection import GridSearchCV

param_grid = {'C': [0.1,1, 10, 100], 'gamma': [1,0.1,0.01,0.001],'kernel': ['sigmoid']}

grid = GridSearchCV(SVC(),param_grid,refit=True,verbose=2)
grid.fit(X_train,y_train)

print(grid.best_estimator_)

import matplotlib.pyplot as plt
grid_predictions = grid.predict(X_test)
print(confusion_matrix(y_test,grid_predictions))
plt.show(sns.heatmap(confusion_matrix(y_test,grid_predictions), annot=True))
print(classification_report(y_test,grid_predictions))
print("Accuracy Score of RBF kernel", accuracy_score(y_test,grid_predictions))

sns.heatmap(cf_matrix, annot=True)

"""### train size : test size = 60% : 40%


"""

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=0)

sigmoid_SVC_classifier.fit(X_train, y_train)

y_pred = sigmoid_SVC_classifier.predict(X_test)
print(f"Accuracy: {100 * accuracy_score(y_test,y_pred)}%\n")
cf_matrix = confusion_matrix(y_test,y_pred)
print("Confusion Matrix:\n", cf_matrix)
print("\nClassification Report:\n")
print(classification_report(y_test,y_pred))

sns.heatmap(cf_matrix, annot=True)

"""### train size : test size = 50% : 50%"""

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=0)

print(len(X_train))
print(len(y_test))

sigmoid_SVC_classifier.fit(X_train, y_train)

y_pred = sigmoid_SVC_classifier.predict(X_test)
print(f"Accuracy: {100 * accuracy_score(y_test,y_pred)}%\n")
cf_matrix = confusion_matrix(y_test,y_pred)
print("Confusion Matrix:\n", cf_matrix)
print("\nClassification Report:\n")
print(classification_report(y_test,y_pred))

sns.heatmap(cf_matrix, annot=True)

"""### train size : test size = 40% : 60%"""

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.6, random_state=0)

print(len(X_train))
print(len(y_test))

sigmoid_SVC_classifier.fit(X_train, y_train)

y_pred = sigmoid_SVC_classifier.predict(X_test)
print(f"Accuracy: {100 * accuracy_score(y_test,y_pred)}%\n")
cf_matrix = confusion_matrix(y_test,y_pred)
print("Confusion Matrix:\n", cf_matrix)
print("\nClassification Report:\n")
print(classification_report(y_test,y_pred))

sns.heatmap(cf_matrix, annot=True)

"""### train size : test size = 30% : 70%"""

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.7, random_state=0)

print(len(X_train))
print(len(y_test))

sigmoid_SVC_classifier.fit(X_train, y_train)

y_pred = sigmoid_SVC_classifier.predict(X_test)
print(f"Accuracy: {100 * accuracy_score(y_test,y_pred)}%\n")
cf_matrix = confusion_matrix(y_test,y_pred)
print("Confusion Matrix:\n", cf_matrix)
print("\nClassification Report:\n")
print(classification_report(y_test,y_pred))

sns.heatmap(cf_matrix, annot=True)

"""# MLP Classifier"""

mlp_classifier = MLPClassifier(learning_rate='constant', max_iter=600)
mlp_classifier

"""### train size : test size = 70% : 30%

"""

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)    # 70% training data, 30% testing data

print(len(X_train))
print(len(y_test))

mlp_classifier.fit(X_train, y_train)

y_pred = mlp_classifier.predict(X_test)
print(f"Accuracy: {100 * accuracy_score(y_test,y_pred)}%\n")
cf_matrix = confusion_matrix(y_test,y_pred)
print("Confusion Matrix:\n")
print(cf_matrix)
print("\nClassification Report:\n")
print(classification_report(y_test,y_pred))

sns.heatmap(cf_matrix, annot=True)

"""### train size : test size = 60% : 40%"""

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=0)    # 60% training data, 40% testing data

print(len(X_train))
print(len(y_test))

mlp_classifier.fit(X_train, y_train)

y_pred = mlp_classifier.predict(X_test)
print(f"Accuracy: {100 * accuracy_score(y_test,y_pred)}%\n")
cf_matrix = confusion_matrix(y_test,y_pred)
print("Confusion Matrix:")
print(cf_matrix)
print("\nClassification Report:\n")
print(classification_report(y_test,y_pred))

sns.heatmap(cf_matrix, annot=True)

"""### train size : test size = 50% : 50%"""

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=0)    # 50% training data, 50% testing data

print(len(X_train))
print(len(y_test))

mlp_classifier.fit(X_train, y_train)

y_pred = mlp_classifier.predict(X_test)
print(f"Accuracy: {100 * accuracy_score(y_test,y_pred)}%\n")
cf_matrix = confusion_matrix(y_test,y_pred)
print("Confusion Matrix:")
print(cf_matrix)
print("\nClassification Report:\n")
print(classification_report(y_test,y_pred))

sns.heatmap(cf_matrix, annot=True)

"""### train size : test size = 40% : 60%"""

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.6, random_state=0)

print(len(X_train))
print(len(y_test))

mlp_classifier.fit(X_train, y_train)

y_pred = mlp_classifier.predict(X_test)
print(f"Accuracy: {100 * accuracy_score(y_test,y_pred)}%\n")
cf_matrix = confusion_matrix(y_test,y_pred)
print("Confusion Matrix:\n")
print(cf_matrix)
print("\nClassification Report:\n")
print(classification_report(y_test,y_pred))

sns.heatmap(cf_matrix, annot=True)

"""### train size : test size = 30% : 70%

"""

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.7, random_state=0)

print(len(X_train))
print(len(y_test))

mlp_classifier.fit(X_train, y_train)

y_pred = mlp_classifier.predict(X_test)
print(f"Accuracy: {100 * accuracy_score(y_test,y_pred)}%\n")
cf_matrix = confusion_matrix(y_test,y_pred)
print("Confusion Matrix:\n")
print(cf_matrix)
print("\nClassification Report:\n")
print(classification_report(y_test,y_pred))

sns.heatmap(cf_matrix, annot=True)

"""# Random Forest Classifier"""

rfc_classifier = RandomForestClassifier(n_estimators=20)
rfc_classifier

"""### train size : test size = 70% : 30%

"""

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)    # 70% training data, 30% testing data

print(len(X_train))
print(len(y_test))

rfc_classifier.fit(X_train, y_train)

y_pred = rfc_classifier.predict(X_test)
print(f"Accuracy: {100 * accuracy_score(y_test,y_pred)}%\n")
cf_matrix = confusion_matrix(y_test,y_pred)
print("Confusion Matrix:\n")
print(cf_matrix)
print("\nClassification Report:\n")
print(classification_report(y_test,y_pred))

sns.heatmap(cf_matrix, annot=True)

"""### train size : test size = 60% : 40%"""

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=0)    # 60% training data, 40% testing data

print(len(X_train))
print(len(y_test))

rfc_classifier.fit(X_train, y_train)

y_pred = rfc_classifier.predict(X_test)
print(f"Accuracy: {100 * accuracy_score(y_test,y_pred)}%\n")
cf_matrix = confusion_matrix(y_test,y_pred)
print("Confusion Matrix:")
print(cf_matrix)
print("\nClassification Report:\n")
print(classification_report(y_test,y_pred))

sns.heatmap(cf_matrix, annot=True)



"""### train size : test size = 50% : 50%"""

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=0)    # 50% training data, 50% testing data

print(len(X_train))
print(len(y_test))

rfc_classifier.fit(X_train, y_train)

y_pred = rfc_classifier.predict(X_test)
print(f"Accuracy: {100 * accuracy_score(y_test,y_pred)}%\n")
cf_matrix = confusion_matrix(y_test,y_pred)
print("Confusion Matrix:")
print(cf_matrix)
print("\nClassification Report:\n")
print(classification_report(y_test,y_pred))

sns.heatmap(cf_matrix, annot=True)

"""### train size : test size = 40% : 60%"""

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.6, random_state=0)

print(len(X_train))
print(len(y_test))

rfc_classifier.fit(X_train, y_train)

y_pred = rfc_classifier.predict(X_test)
print(f"Accuracy: {100 * accuracy_score(y_test,y_pred)}%\n")
cf_matrix = confusion_matrix(y_test,y_pred)
print("Confusion Matrix:\n")
print(cf_matrix)
print("\nClassification Report:\n")
print(classification_report(y_test,y_pred))

sns.heatmap(cf_matrix, annot=True)

"""### train size : test size = 30% : 70%"""

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.7, random_state=0)

print(len(X_train))
print(len(y_test))

rfc_classifier.fit(X_train, y_train)

y_pred = rfc_classifier.predict(X_test)
print(f"Accuracy: {100 * accuracy_score(y_test,y_pred)}%\n")
cf_matrix = confusion_matrix(y_test,y_pred)
print("Confusion Matrix:\n")
print(cf_matrix)
print("\nClassification Report:\n")
print(classification_report(y_test,y_pred))

sns.heatmap(cf_matrix, annot=True)