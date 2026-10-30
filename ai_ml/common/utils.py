import numpy as np


def compute_cost(X, y, w, b):
    """
    compute cost
    Args:
      X (ndarray (m,n)): Data, m examples with n features
      y (ndarray (m,)) : target values
      w (ndarray (n,)) : model parameters
      b (scalar)       : model parameter
    Returns
      cost (scalar)    : cost
    """
    m = X.shape[0]
    cost = 0.0
    for i in range(m):
        f_wb_i = np.dot(X[i], w) + b  # (n,)(n,)=scalar
        cost = cost + (f_wb_i - y[i]) ** 2
    cost = cost / (2 * m)
    return cost


# Feature scaling (mean normalization)
def normalize(X):
    mean = np.mean(X, axis=0)
    std = np.std(X, axis=0)

    # avoid division by zero
    std[std == 0] = 1

    return (X - mean) / std, mean, std


# Add column of 1s for bias term
def add_bias_column(X):
    ones = np.ones((X.shape[0], 1))
    return np.hstack((ones, X))


# Sigmoid
def sigmoid(z):
    return 1 / (1 + np.exp(-z))


def inbounds(a, b, xlim, ylim):
    xlow, xhigh = xlim
    ylow, yhigh = ylim
    ax, ay = a
    bx, by = b
    if (
        (ax > xlow and ax < xhigh)
        and (bx > xlow and bx < xhigh)
        and (ay > ylow and ay < yhigh)
        and (by > ylow and by < yhigh)
    ):
        return True
    return False
