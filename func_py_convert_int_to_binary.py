# func_py_convert_int_to_binary.py
def func_py_convert_int_to_binary(n):
    try:
        return bin(n)
    except TypeError:
        return None

print(func_py_convert_int_to_binary(10))
print(func_py_convert_int_to_binary(255))
