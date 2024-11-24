import numpy as np
from sklearn.datasets import load_iris, load_wine, load_breast_cancer
from sklearn.model_selection import train_test_split, cross_val_score, KFold, LeaveOneOut
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.kernel_approximation import RBFSampler
from sklearn.linear_model import SGDClassifier

#Cargar datasets
datasets = {
    "Iris": load_iris(),
    "Wine": load_wine(),
    "Breast Cancer": load_breast_cancer()
}

#Configuracion de clasificadores
results = {}
for name, dataset in datasets.items():
    X, y = dataset.data, dataset.target

    #Perceptron Multicapa (MLPClassifier)
    mlp = MLPClassifier(hidden_layer_sizes=(10,), max_iter=1000, random_state=42)

    #Red Neuronal RBF usando RBFSampler
    rbf_feature = RBFSampler(gamma=1, random_state=42)
    X_rbf = rbf_feature.fit_transform(X)
    rbf = SGDClassifier(max_iter=1000, tol=1e-3, random_state=42)

    #Validacion
    results[name] = {}
    for clf_name, clf, data in [("MLP", mlp, X), ("RBF", rbf, X_rbf)]:
        print(f"\n===== Dataset: {name} | Clasificador: {clf_name} =====")
        results[name][clf_name] = {}

        # Hold-Out 70/30
        X_train, X_test, y_train, y_test = train_test_split(data, y, test_size=0.3, random_state=42)
        clf.fit(X_train, y_train)
        y_pred = clf.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        conf_matrix = confusion_matrix(y_test, y_pred)
        print(f"Hold-Out 70/30 - Accuracy: {accuracy:.4f}")
        print(f"Hold-Out 70/30 - Matriz de Confusión:\n{conf_matrix}")
        results[name][clf_name]["Hold-Out"] = (accuracy, conf_matrix)

        # 10-Fold Cross-V
        kf = KFold(n_splits=10, shuffle=True, random_state=42)
        scores = cross_val_score(clf, data, y, cv=kf)
        print(f"10-Fold Cross-Validation - Accuracy promedio: {np.mean(scores):.4f}")
        results[name][clf_name]["10-Fold"] = np.mean(scores)

        # Leave-One-Out
        loo = LeaveOneOut()
        scores = cross_val_score(clf, data, y, cv=loo)
        print(f"Leave-One-Out - Accuracy promedio: {np.mean(scores):.4f}")
        results[name][clf_name]["Leave-One-Out"] = np.mean(scores)

#Resultados finales
print("\n=== Resultados Finales ===")
for dataset_name, classifiers in results.items():
    print(f"\nDataset: {dataset_name}")
    for clf_name, metrics in classifiers.items():
        print(f"\n  Clasificador: {clf_name}")
        for validation, result in metrics.items():
            if validation == "Hold-Out":
                accuracy, conf_matrix = result
                print(f"    {validation} - Accuracy: {accuracy:.4f}")
                print(f"    {validation} - Matriz de Confusión:\n{conf_matrix}")
            else:
                print(f"    {validation} - Accuracy promedio: {result:.4f}")
