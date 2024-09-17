# func_py_remove_duplicates.py
def func_py_remove_duplicates(lst):
    return list(dict.fromkeys(lst))

print(func_py_remove_duplicates([10, 20, 20, 30, 40, 40]))
