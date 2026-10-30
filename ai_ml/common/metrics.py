import numpy as np


# MSE - Mean Squared Error
def mean_squared_error(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)


# Accuracy
def accuracy(y_true, y_pred):
    return np.mean(y_true == y_pred)


# inary cross entropy
def binary_cross_entropy(y_true, y_pred):
    epsilon = 1e-15  # avoid log(0)
    y_pred = np.clip(y_pred, epsilon, 1 - epsilon)

    return -np.mean(y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred))
