# fun_sort_list_of_tuples.py
def fun_sort_list_of_tuples(lst):
    return sorted(lst, key=lambda x: x[1])

print(fun_sort_list_of_tuples([(1, 3), (3, 2), (2, 1)]))
