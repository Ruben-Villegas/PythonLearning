# func_py_check_armstrong_number.py
def func_py_check_armstrong_number(n):
    num_digits = len(str(n))
    return n == sum(int(digit) ** num_digits for digit in str(n))

print(func_py_check_armstrong_number(153))
