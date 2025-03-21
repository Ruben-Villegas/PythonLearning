# fun_py_find_gcd.py

import math

def fun_py_find_gcd(a, b):
    return math.gcd(a, b)

def test_find_gcd():
    pairs = [(24, 36), (100, 25), (81, 27)]
    for a, b in pairs:
        print(f"GCD of {a} and {b}: {fun_py_find_gcd(a, b)}")

if __name__ == "__main__":
    test_find_gcd()
