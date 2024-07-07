# fun_lcm.py
def fun_lcm(a, b):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    return abs(a * b) // gcd(a, b)

print(fun_lcm(48, 18))
