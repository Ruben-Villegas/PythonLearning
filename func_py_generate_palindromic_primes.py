# func_py_generate_palindromic_primes.py
def func_py_generate_palindromic_primes(limit):
    def is_palindrome(n):
        return str(n) == str(n)[::-1]
    
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    return [num for num in range(2, limit) if is_palindrome(num) and is_prime(num)]

print(func_py_generate_palindromic_primes(1000))
