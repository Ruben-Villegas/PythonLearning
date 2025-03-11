# func_py_detect_language.py
from langdetect import detect

def func_py_detect_language(text):
    return detect(text)

print(func_py_detect_language("Bonjour tout le monde"))
