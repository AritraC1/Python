import numpy as np
from mini_systems.regression.linear_regression import LinearRegression
from visualize import plot_cost

# Dummy data (y = 2x)
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])

model = LinearRegression(lr=0.05, iterations=50)
model.fit(x, y)

preds = model.predict(x)

print("Final w:", model.w)
print("Final b:", model.b)
print("Predictions:", preds)

plot_cost(model.cost_history)
