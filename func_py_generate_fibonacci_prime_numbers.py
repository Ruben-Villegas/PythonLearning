# func_py_generate_fibonacci_prime_numbers.py
def func_py_generate_fibonacci_prime_numbers(limit):
    def is_prime(n):
        return n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))

    fib_primes = []
    a, b = 0, 1
    while a <= limit:
        if is_prime(a):
            fib_primes.append(a)
        a, b = b, a + b
    return fib_primes

print(func_py_generate_fibonacci_prime_numbers(1000))
