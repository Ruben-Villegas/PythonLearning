# func_py_find_unique_character.py
def func_py_find_unique_characters(s):
    return "".join(sorted(set(s)))

print(func_py_find_unique_characters("mississippi"))
