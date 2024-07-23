# fun_py_generate_random_string.py
import random
import string

def fun_py_generate_random_string(length):
    return ''.join(random.choice(string.ascii_letters) for i in range(length))

print(fun_py_generate_random_string(8))
