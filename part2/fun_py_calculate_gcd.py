# fun_py_calculate_gcd.py

import math

def fun_py_calculate_gcd(a, b):
    return math.gcd(a, b)

def test_calculate_gcd():
    num1, num2 = 48, 18
    print(f"GCD of {num1} and {num2}: {fun_py_calculate_gcd(num1, num2)}")

if __name__ == "__main__":
    test_calculate_gcd()
