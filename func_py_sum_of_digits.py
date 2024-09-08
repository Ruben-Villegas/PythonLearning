# func_py_sum_of_digits.py
def func_py_sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

print(func_py_sum_of_digits(1234))
