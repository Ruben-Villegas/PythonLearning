# func_generate_powers.py
def func_generate_powers(base, exponent):
    return [base ** i for i in range(exponent + 1)]

print(func_generate_powers(2, 5))
