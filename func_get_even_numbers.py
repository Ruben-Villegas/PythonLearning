# func_get_even_numbers.py
def func_get_even_numbers(lst):
    return [i for i in lst if i % 2 == 0]

print(func_get_even_numbers([1, 2, 3, 4, 5, 6]))
