import numpy as np

# Implement linear regression + gradient descent from scratch
class LinearRegression:
    # What the model KNOWS (state) ?
    def __init__(self, lr=0.1, iterations=1000):
        self.lr = lr
        self.iterations = iterations
        self.w = None
        self.b = None
        self.cost_history = []

    # What the model DOES?
    def predict(self, X):
        y = np.dot(X, self.w) + self.b
        return y

    def compute_cost(self, y, y_pred):
        m = len(y)
        cost = (1 / m) * (np.sum((y_pred - y) ** 2))
        return cost

    # the model learns from data
    # adjust internal parameters so predictions become accurate
    def fit(self, X, y):
        m = len(X)

        # Initialise parameters
        self.w = 0.0
        self.b = 0.0

        for i in range(self.iterations):
            # Step 1: Prediction
            y_pred = self.predict(X)

            # Step 2: Cost
            cost = self.compute_cost(y, y_pred)
            self.cost_history.append(cost)

            # Step 3: Gradient
            dw = (2 / m) * np.sum((y_pred - y) * X)
            db = (2 / m) * np.sum(y_pred - y)

            # Step 4: Update
            self.w = self.w - self.lr * dw
            self.b = self.b - self.lr * db

            # Optional logging
            if i % 100 == 0:
                print(f"Iteration {i} | Cost: {cost:.4f}")

        return self
