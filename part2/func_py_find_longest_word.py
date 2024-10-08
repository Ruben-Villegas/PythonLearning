# func_py_find_longest_word.py
def func_py_find_longest_word(sentence):
    words = sentence.split()
    longest_word = max(words, key=len)
    return longest_word
