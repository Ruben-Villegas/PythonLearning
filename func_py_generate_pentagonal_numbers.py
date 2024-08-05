# func_py_generate_pentagonal_numbers.py
def func_py_generate_pentagonal_numbers(n):
    return [i * (3 * i - 1) // 2 for i in range(1, n+1)]

print(func_py_generate_pentagonal_numbers(10))
