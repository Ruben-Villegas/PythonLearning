# func_py_find_first_non_repeating_char.py
def func_py_find_first_non_repeating_char(s):
    for char in s:
        if s.count(char) == 1:
            return char
    return None

print(func_py_find_first_non_repeating_char("swiss"))
