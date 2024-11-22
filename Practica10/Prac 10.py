import numpy as np
from sklearn.datasets import load_iris, load_wine, load_breast_cancer
from sklearn.model_selection import train_test_split, KFold, LeaveOneOut
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

#Cargar datasets
datasets = {
    'Iris': load_iris(),
    'Wine': load_wine(),
    'Breast Cancer': load_breast_cancer()
}

#Funcion de evaluacion
def evaluate_classifier(classifier, X, y, method='holdout'):
    if method == 'holdout':
        #Hold-Out 70/30
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
        classifier.fit(X_train, y_train)
        y_pred = classifier.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        cm = confusion_matrix(y_test, y_pred)
    elif method == 'kfold':
        #10-Fold Cross-V
        kf = KFold(n_splits=10, random_state=42, shuffle=True)
        y_true, y_pred = [], []
        for train_index, test_index in kf.split(X):
            X_train, X_test = X[train_index], X[test_index]
            y_train, y_test = y[train_index], y[test_index]
            classifier.fit(X_train, y_train)
            y_pred_fold = classifier.predict(X_test)
            y_true.extend(y_test)
            y_pred.extend(y_pred_fold)
        accuracy = accuracy_score(y_true, y_pred)
        cm = confusion_matrix(y_true, y_pred)
    elif method == 'leaveoneout':
        #Leave-One-Out Cross-V
        loo = LeaveOneOut()
        y_true, y_pred = [], []
        for train_index, test_index in loo.split(X):
            X_train, X_test = X[train_index], X[test_index]
            y_train, y_test = y[train_index], y[test_index]
            classifier.fit(X_train, y_train)
            y_pred.append(classifier.predict(X_test)[0])
            y_true.append(y_test[0])
        accuracy = accuracy_score(y_true, y_pred)
        cm = confusion_matrix(y_true, y_pred)
    return accuracy, cm

#Parametro K(KNN)
K = 5  #Ajustable

#Clasificadores en los datasets con cada metodo de validacion
results = []
for dataset_name, dataset in datasets.items():
    X, y = dataset.data, dataset.target
    for classifier_name, classifier in [
        ('Naive Bayes', GaussianNB()),
        ('KNN', KNeighborsClassifier(n_neighbors=K))
    ]:
        for method in ['holdout', 'kfold', 'leaveoneout']:
            accuracy, cm = evaluate_classifier(classifier, X, y, method)
            results.append({
                'Dataset': dataset_name,
                'Classifier': classifier_name,
                'Validation Method': method,
                'Accuracy': accuracy,
                'Confusion Matrix': cm
            })

#Resultados
for result in results:
    print(f"Dataset: {result['Dataset']}, Clasificador: {result['Classifier']}, Metodo: {result['Validation Method']}")
    print(f"Accuracy: {result['Accuracy']}")
    print("Matriz de Confusion:")
    print(result['Confusion Matrix'])
    print("-" * 40)
