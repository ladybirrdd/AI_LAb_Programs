from sklearn.neural_network import MLPClassifier
import numpy as np

X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y_and, y_or = np.array([0, 0, 0, 1]), np.array([0, 1, 1, 1])

nn_and = MLPClassifier(hidden_layer_sizes=(2,), max_iter=2000, learning_rate_init=0.001, solver='lbfgs').fit(X, y_and)
print("AND Gate Predictions:", nn_and.predict(X))

nn_or = MLPClassifier(hidden_layer_sizes=(2,), max_iter=2000, learning_rate_init=0.001, solver='lbfgs').fit(X, y_or)
print("OR Gate Predictions:", nn_or.predict(X))
