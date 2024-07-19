# func_find_hcf.py
def func_find_hcf(a, b):
    while b:
        a, b = b, a % b
    return a

print(func_find_hcf(24, 36))
