# func_py_prime_numbers.py

def func_py_prime_numbers(n):
    primes = []
    for num in range(2, n + 1):
        if all(num % p != 0 for p in primes):
            primes.append(num)
    return primes

def test_prime_numbers():
    print(f"Prime numbers up to 50: {func_py_prime_numbers(50)}")

if __name__ == "__main__":
    test_prime_numbers()
