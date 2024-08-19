# func_py_generate_undulating_numbers.py
def func_py_generate_undulating_numbers(d1, d2, n):
    return [int(str(d1) + str(d2) * (i % 2)) for i in range(1, n + 1)]

print(func_py_generate_undulating_numbers(1, 2, 10))
