# func_py_calculate_folium_of_descartes.py
import matplotlib.pyplot as plt
import numpy as np

def func_py_calculate_folium_of_descartes(a, points):
    t = np.linspace(-2, 2, points)
    x = (3 * a * t) / (1 + t**3)
    y = (3 * a * t**2) / (1 + t**3)
    plt.plot(x, y)
    plt.title("Folium of Descartes")
    plt.show()

func_py_calculate_folium_of_descartes(5, 1000)
