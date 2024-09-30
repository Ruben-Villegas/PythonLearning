# func_py_calculate_power.py
def func_py_calculate_power(base, exp):
    result = 1
    for _ in range(exp):
        result *= base
    return result
