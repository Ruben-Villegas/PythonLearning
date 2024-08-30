# func_py_calculate_butterfly_curve.py
import matplotlib.pyplot as plt
import numpy as np

def func_py_calculate_butterfly_curve(points):
    t = np.linspace(0, 12 * np.pi, points)
    x = np.sin(t) * (np.exp(np.cos(t)) - 2 * np.cos(4 * t) - np.sin(t/12)**5)
    y = np.cos(t) * (np.exp(np.cos(t)) - 2 * np.cos(4 * t) - np.sin(t/12)**5)
    plt.plot(x, y)
    plt.title("Butterfly Curve")
    plt.show()

func_py_calculate_butterfly_curve(1000)
