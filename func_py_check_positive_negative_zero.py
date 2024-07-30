# func_py_check_positive_negative_zero.py
def func_py_check_positive_negative_zero(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

print(func_py_check_positive_negative_zero(10))
print(func_py_check_positive_negative_zero(-5))
print(func_py_check_positive_negative_zero(0))
