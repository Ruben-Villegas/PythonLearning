# func_find_duplicates.py
def func_find_duplicates(lst):
    return list(set([item for item in lst if lst.count(item) > 1]))

print(func_find_duplicates([1, 2, 2, 3, 4, 4, 5]))
