def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def main():
    terms = 10
    print(f"Fibonacci sequence up to {terms} terms:")
    for i in range(terms):
        print(fibonacci(i), end=" ")

if __name__ == "__main__":
    main()
