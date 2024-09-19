# func_py_remove_vowels.py
def func_py_remove_vowels(sentence):
    return ''.join([char for char in sentence if char.lower() not in 'aeiou'])

print(func_py_remove_vowels("Python programming is fun"))
