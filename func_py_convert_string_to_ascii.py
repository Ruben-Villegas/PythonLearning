# func_py_convert_string_to_ascii.py
def func_py_convert_string_to_ascii(s):
    return [ord(char) for char in s]

print(func_py_convert_string_to_ascii("Python"))
