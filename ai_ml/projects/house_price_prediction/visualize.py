import matplotlib.pyplot as plt


def plot_cost(cost_history):
    plt.plot(cost_history)
    plt.xlabel("Iterations")
    plt.ylabel("Cost")
    plt.title("Cost vs Iterations")
    plt.show()
