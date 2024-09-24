# func_py_find_largest_odd.py
def func_py_find_largest_odd(numbers):
    odds = [num for num in numbers if num % 2 != 0]
    return max(odds) if odds else None

print(func_py_find_largest_odd([1, 2, 3, 4, 5]))
