# func_py_find_deficient_primes.py
def func_py_find_deficient_primes(limit):
    primes = []
    for num in range(2, limit):
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break
        else:
            if sum([i for i in range(1, num) if num % i == 0]) < num:
                primes.append(num)
    return primes

print(func_py_find_deficient_primes(100))
