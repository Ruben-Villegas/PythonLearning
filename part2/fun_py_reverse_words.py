# fun_py_reverse_words.py

def fun_py_reverse_words(s):
    return " ".join(s.split()[::-1])

def test_reverse_words():
    text = "Hello world this is Python"
    print(f"Reversed words: {fun_py_reverse_words(text)}")

if __name__ == "__main__":
    test_reverse_words()
