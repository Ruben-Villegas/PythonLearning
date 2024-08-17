# func_py_calculate_superellipsoid_volume.py
import math

def func_py_calculate_superellipsoid_volume(a, b, c, n):
    k1 = (math.gamma(1 + 1/n))**3
    return 8 * a * b * c * k1 / math.gamma(1 + 3/n)

print(func_py_calculate_superellipsoid_volume(3, 4, 5, 2))
