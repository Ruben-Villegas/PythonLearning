# func_convert_list_to_dict.py
def func_convert_list_to_dict(lst):
    return {i: lst[i] for i in range(len(lst))}

print(func_convert_list_to_dict(['a', 'b', 'c', 'd']))
