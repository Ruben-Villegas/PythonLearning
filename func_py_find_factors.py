# func_py_find_factors.py
def func_py_find_factors(num):
    return [i for i in range(1, num + 1) if num % i == 0]

print(func_py_find_factors(28))
