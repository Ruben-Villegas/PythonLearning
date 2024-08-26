# func_py_calculate_elliptic_cone_volume.py
import math

def func_py_calculate_elliptic_cone_volume(radius_a, radius_b, height):
    return (1/3) * math.pi * radius_a * radius_b * height

print(func_py_calculate_elliptic_cone_volume(3, 4, 7))
