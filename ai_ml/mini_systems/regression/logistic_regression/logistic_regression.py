import numpy as np


# Logistic Regression: Single most widely used Classification Algorithm
class LogisticRegression:
    # What the model KNOWS (state) ?
    def __init__(self, lr=0.1, iterations=1000):
        self.lr = lr
        self.iterations = iterations
        self.w = None
        self.b = None
        self.g = None
        self.cost_history = []

    # What the model DOES?
    def predict(self, X):
        z = np.dot(X, self.w) + self.b
        return 1 / (1 + np.exp(-z))

    def compute_cost(self, y, y_pred):
        m = len(y)
        epsilon = 1e-15
        y_pred = np.clip(y_pred, epsilon, 1 - epsilon)
        cost = -(1 / m) * np.sum(y * np.log(y_pred) + (1 - y) * np.log(1 - y_pred))
        return cost

    # the model learns from data
    # adjust internal parameters so predictions become accurate
    def fit(self, X, y):
        m = X.shape[0]
        n = X.shape[1]

        # Initialise parameters
        self.w = np.zeros(n)
        self.b = 0.0

        for i in range(self.iterations):
            # Step 1: Prediction
            y_pred = self.predict(X)

            # Step 2: Cost
            cost = self.compute_cost(y, y_pred)
            self.cost_history.append(cost)

            # Step 3: Gradient
            dw = (1 / m) * np.dot(X.T, (y_pred - y))
            db = (1 / m) * np.sum(y_pred - y)

            # Step 4: Update
            self.w = self.w - self.lr * dw
            self.b = self.b - self.lr * db

        return self
