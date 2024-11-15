import numpy as np
import pandas as pd
from sklearn.datasets import load_iris, load_wine, load_breast_cancer
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split, KFold, LeaveOneOut
from scipy.spatial import distance
from collections import Counter
datasets = {
    'Iris': load_iris(),
    'Wine': load_wine(),
    'Breast Cancer': load_breast_cancer()
}

#Clasificador Euclidiano y 1NN
class EuclideanClassifier:
    def __init__(self, data, labels):
        self.centroids = {}
        for label in np.unique(labels):
            self.centroids[label] = data[labels == label].mean(axis=0)

    def predict(self, x):
        distances = {label: distance.euclidean(x, centroid) for label, centroid in self.centroids.items()}
        return min(distances, key=distances.get)

class NearestNeighborClassifier:
    def __init__(self, train_data, train_labels):
        self.train_data = train_data
        self.train_labels = train_labels

    def predict(self, x):
        distances = [distance.euclidean(x, train_x) for train_x in self.train_data]
        return self.train_labels[np.argmin(distances)]

#Funcion de evaluacion para cada metodo de validacion
def evaluate_classifier(classifier_type, X, y, method='holdout'):
    if classifier_type == 'Euclidean':
        clf_class = EuclideanClassifier
    elif classifier_type == '1NN':
        clf_class = NearestNeighborClassifier

    if method == 'holdout':
        #Hold-Out70/30
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
        if classifier_type == 'Euclidean':
            clf = clf_class(X_train, y_train)
            y_pred = [clf.predict(x) for x in X_test]
        else:
            clf = clf_class(X_train, y_train)
            y_pred = [clf.predict(x) for x in X_test]
        accuracy = accuracy_score(y_test, y_pred)
        cm = confusion_matrix(y_test, y_pred)
    
    elif method == 'kfold':
        #10-Fold-Cross-Validation
        kf = KFold(n_splits=10, random_state=42, shuffle=True)
        y_true, y_pred = [], []
        for train_index, test_index in kf.split(X):
            X_train, X_test = X[train_index], X[test_index]
            y_train, y_test = y[train_index], y[test_index]
            clf = clf_class(X_train, y_train)
            y_pred_fold = [clf.predict(x) for x in X_test]
            y_true.extend(y_test)
            y_pred.extend(y_pred_fold)
        accuracy = accuracy_score(y_true, y_pred)
        cm = confusion_matrix(y_true, y_pred)

    elif method == 'leaveoneout':
        #Leave-One-Out Cross-Validation
        loo = LeaveOneOut()
        y_true, y_pred = [], []
        for train_index, test_index in loo.split(X):
            X_train, X_test = X[train_index], X[test_index]
            y_train, y_test = y[train_index], y[test_index]
            clf = clf_class(X_train, y_train)
            y_pred.append(clf.predict(X_test[0]))
            y_true.append(y_test[0])
        accuracy = accuracy_score(y_true, y_pred)
        cm = confusion_matrix(y_true, y_pred)

    return accuracy, cm

#Probar clasificadores en los datasets con cada metodo de validacion
results = []
for dataset_name, dataset in datasets.items():
    X, y = dataset.data, dataset.target
    for classifier_type in ['Euclidean', '1NN']:
        for method in ['holdout', 'kfold', 'leaveoneout']:
            accuracy, cm = evaluate_classifier(classifier_type, X, y, method)
            results.append({
                'Dataset': dataset_name,
                'Classifier': classifier_type,
                'Validation Method': method,
                'Accuracy': accuracy,
                'Confusion Matrix': cm
            })

#Impresion
for result in results:
    print(f"Dataset: {result['Dataset']}, Classifier: {result['Classifier']}, Method: {result['Validation Method']}")
    print(f"Accuracy: {result['Accuracy']}")
    print("Confusion Matrix:")
    print(result['Confusion Matrix'])
    print("-" * 40)
