# func_py_find_largest_file.py
import os

def func_py_find_largest_file(directory):
    largest_file = max(
        (os.path.join(directory, f) for f in os.listdir(directory)),
        key=os.path.getsize,
        default=None
    )
    return largest_file

print(func_py_find_largest_file("."))
