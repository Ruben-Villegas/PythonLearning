# func_py_find_powerful_numbers.py
def func_py_find_powerful_numbers(limit):
    def is_powerful(n):
        for prime_factor in range(2, n):
            if n % prime_factor == 0:
                if n % (prime_factor ** 2) != 0:
                    return False
        return True
    
    return [n for n in range(1, limit) if is_powerful(n)]

print(func_py_find_powerful_numbers(100))
