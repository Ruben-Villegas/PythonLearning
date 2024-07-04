# generate_and_find_max.py
import random

def generate_random_list(size, start, end):
    return [random.randint(start, end) for _ in range(size)]

def find_max(lst):
    return max(lst)

if __name__ == "__main__":
    size = int(input("Enter the size of the list: "))
    start = int(input("Enter the start range: "))
    end = int(input("Enter the end range: "))
    random_list = generate_random_list(size, start, end)
    print(f"Generated list: {random_list}")
    maximum = find_max(random_list)
    print(f"Maximum value in the list: {maximum}")
