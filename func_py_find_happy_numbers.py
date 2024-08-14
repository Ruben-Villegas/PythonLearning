# func_py_find_happy_numbers.py
def func_py_find_happy_numbers(limit):
    def is_happy(num):
        visited = set()
        while num != 1 and num not in visited:
            visited.add(num)
            num = sum(int(i) ** 2 for i in str(num))
        return num == 1
    
    return [i for i in range(1, limit) if is_happy(i)]

print(func_py_find_happy_numbers(100))
