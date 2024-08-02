# func_py_find_hcf.py
def func_py_find_hcf(a, b):
    while b:
        a, b = b, a % b
    return a

print(func_py_find_hcf(54, 24))
