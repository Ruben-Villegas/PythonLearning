def func_py_generate_prime_numbers(limit):
    primes = []
    for num in range(2, limit + 1):
        if all(num % i != 0 for i in range(2, int(num**0.5) + 1)):
            primes.append(num)
    return primes
