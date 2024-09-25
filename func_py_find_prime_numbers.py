# func_py_find_prime_numbers.py
def func_py_find_prime_numbers(n):
    primes = []
    for num in range(2, n + 1):
        if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
            primes.append(num)
    return primes

print(func_py_find_prime_numbers(20))
