# func_py_generate_hyperbolic_numbers.py
def func_py_generate_hyperbolic_numbers(limit):
    hyperbolic_numbers = [n for n in range(1, limit + 1) if n * (n + 1) == limit]
    return hyperbolic_numbers

print(func_py_generate_hyperbolic_numbers(1000))
