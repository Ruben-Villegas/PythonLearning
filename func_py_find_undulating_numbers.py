# func_py_find_undulating_numbers.py
def func_py_find_undulating_numbers(limit):
    return [n for n in range(10, limit) if str(n)[0] != str(n)[1] and all(digit == str(n)[i % 2] for i, digit in enumerate(str(n)))]

print(func_py_find_undulating_numbers(1000))
