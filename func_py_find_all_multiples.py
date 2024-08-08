# func_py_find_all_multiples.py
def func_py_find_all_multiples(n, limit):
    return [i for i in range(n, limit + 1, n)]

print(func_py_find_all_multiples(3, 30))
