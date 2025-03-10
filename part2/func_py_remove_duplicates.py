# func_py_remove_duplicates.py
def func_py_remove_duplicates(lst):
    return list(dict.fromkeys(lst))

print(func_py_remove_duplicates([1, 2, 2, 3, 4, 4, 5]))
