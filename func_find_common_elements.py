# func_find_common_elements.py
def func_find_common_elements(lst1, lst2):
    return list(set(lst1) & set(lst2))

print(func_find_common_elements([1, 2, 3], [2, 3, 4]))
