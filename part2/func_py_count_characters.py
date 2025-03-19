# func_py_count_characters.py

def func_py_count_characters(s):
    return {char: s.count(char) for char in set(s)}

def test_count_characters():
    text = "hello world"
    print(func_py_count_characters(text))

if __name__ == "__main__":
    test_count_characters()
