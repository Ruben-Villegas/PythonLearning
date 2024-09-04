# func_py_calculate_apollonian_gasket.py
import matplotlib.pyplot as plt
import numpy as np

def func_py_calculate_apollonian_gasket(a, b, c, depth):
    def next_curvature(a, b, c):
        return a + b + c + 2 * np.sqrt(a * b + b * c + c * a)

    def draw_circle(ax, k, center, color='black'):
        circle = plt.Circle(center, 1/np.abs(k), color=color, fill=False)
        ax.add_artist(circle)

    def recurse(ax, a, b, c, depth):
        if depth == 0:
            return
        d = next_curvature(a, b, c)
        center_d = ((1 / d) * (np.sqrt((a + b + c + d) * a * b * c)))
        draw_circle(ax, d, center_d)
        recurse(ax, a, b, d, depth - 1)
        recurse(ax, a, c, d, depth - 1)
        recurse(ax, b, c, d, depth - 1)

    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    recurse(ax, a, b, c, depth)
    plt.xlim(-1.5, 1.5)
    plt.ylim(-1.5, 1.5)
    plt.title("Apollonian Gasket")
    plt.show()

func_py_calculate_apollonian_gasket(1, 1, 1, 4)
