import numpy as np
import matplotlib.pyplot as plt
from common.utils import compute_cost, inbounds
from common.colors import DLColors


# draw derivative line
# y = m*(x - x1) + y1
def add_line(dj_dx, x1, y1, d, ax):
    x = np.linspace(x1 - d, x1 + d, 50)
    y = dj_dx * (x - x1) + y1
    ax.scatter(x1, y1, color=DLColors.dlblue, s=50)
    ax.plot(x, y, "--", c=DLColors.dldarkred, zorder=10, linewidth=1)
    xoff = 30 if x1 == 200 else 10
    ax.annotate(
        r"$\frac{\partial J}{\partial w}$ =%d" % dj_dx,
        fontsize=14,
        xy=(x1, y1),
        xycoords="data",
        xytext=(xoff, 10),
        textcoords="offset points",
        arrowprops=dict(arrowstyle="->"),
        horizontalalignment="left",
        verticalalignment="top",
    )


def plt_gradients(x_train, y_train, f_compute_cost, f_compute_gradient):
    # ===============
    #  First subplot
    # ===============
    fig, ax = plt.subplots(1, 2, figsize=(12, 4))

    # Print w vs cost to see minimum
    fix_b = 100
    w_array = np.linspace(-100, 500, 50)
    w_array = np.linspace(0, 400, 50)
    cost = np.zeros_like(w_array)

    for i in range(len(w_array)):
        tmp_w = w_array[i]
        cost[i] = f_compute_cost(x_train, y_train, tmp_w, fix_b)
    ax[0].plot(w_array, cost, linewidth=1)
    ax[0].set_title("Cost vs w, with gradient; b set to 100")
    ax[0].set_ylabel("Cost")
    ax[0].set_xlabel("w")

    # plot lines for fixed b=100
    for tmp_w in [100, 200, 300]:
        fix_b = 100
        dj_dw, dj_db = f_compute_gradient(x_train, y_train, tmp_w, fix_b)
        j = f_compute_cost(x_train, y_train, tmp_w, fix_b)
        add_line(dj_dw, tmp_w, j, 30, ax[0])

    # ===============
    # Second Subplot
    # ===============

    tmp_b, tmp_w = np.meshgrid(np.linspace(-200, 200, 10), np.linspace(-100, 600, 10))
    U = np.zeros_like(tmp_w)
    V = np.zeros_like(tmp_b)
    for i in range(tmp_w.shape[0]):
        for j in range(tmp_w.shape[1]):
            U[i][j], V[i][j] = f_compute_gradient(
                x_train, y_train, tmp_w[i][j], tmp_b[i][j]
            )
    X = tmp_w
    Y = tmp_b
    n = -2
    color_array = np.sqrt(((V - n) / 2) ** 2 + ((U - n) / 2) ** 2)

    ax[1].set_title("Gradient shown in quiver plot")
    Q = ax[1].quiver(
        X,
        Y,
        U,
        V,
        color_array,
        units="width",
    )
    ax[1].quiverkey(
        Q, 0.9, 0.9, 2, r"$2 \frac{m}{s}$", labelpos="E", coordinates="figure"
    )
    ax[1].set_xlabel("w")
    ax[1].set_ylabel("b")


def plt_contour_wgrad(
    x,
    y,
    hist,
    ax,
    w_range=[-100, 500, 5],
    b_range=[-500, 500, 5],
    contours=[0.1, 50, 1000, 5000, 10000, 25000, 50000],
    resolution=5,
    w_final=200,
    b_final=100,
    step=10,
):
    b0, w0 = np.meshgrid(np.arange(*b_range), np.arange(*w_range))
    z = np.zeros_like(b0)
    for i in range(w0.shape[0]):
        for j in range(w0.shape[1]):
            z[i][j] = compute_cost(x, y, w0[i][j], b0[i][j])

    CS = ax.contour(
        w0,
        b0,
        z,
        contours,
        linewidths=2,
        colors=[
            DLColors.dlblue,
            DLColors.dlorange,
            DLColors.dldarkred,
            DLColors.dlmagenta,
            DLColors.dlpurple,
        ],
    )
    ax.clabel(CS, inline=1, fmt="%1.0f", fontsize=10)
    ax.set_xlabel("w")
    ax.set_ylabel("b")
    ax.set_title("Contour plot of cost J(w,b), vs b,w with path of gradient descent")
    w = w_final
    b = b_final
    ax.hlines(b, ax.get_xlim()[0], w, lw=2, color=DLColors.dlpurple, ls="dotted")
    ax.vlines(w, ax.get_ylim()[0], b, lw=2, color=DLColors.dlpurple, ls="dotted")

    base = hist[0]
    for point in hist[0::step]:
        edist = np.sqrt((base[0] - point[0]) ** 2 + (base[1] - point[1]) ** 2)
        if edist > resolution or point == hist[-1]:
            if inbounds(point, base, ax.get_xlim(), ax.get_ylim()):
                plt.annotate(
                    "",
                    xy=point,
                    xytext=base,
                    xycoords="data",
                    arrowprops={"arrowstyle": "->", "color": "r", "lw": 3},
                    va="center",
                    ha="center",
                )
            base = point
    return
