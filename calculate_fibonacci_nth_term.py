# calculate_fibonacci_nth_term.py
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

if __name__ == "__main__":
    n = int(input("Enter the position of Fibonacci sequence: "))
    fib_n = fibonacci(n)
    print(f"The {n}th term in the Fibonacci sequence is {fib_n}")
