# func_py_calculate_hollow_cylinder_volume.py
import math

def func_py_calculate_hollow_cylinder_volume(outer_radius, inner_radius, height):
    return math.pi * height * (outer_radius**2 - inner_radius**2)

print(func_py_calculate_hollow_cylinder_volume(5, 3, 10))
