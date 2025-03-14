# func_py_caesar_cipher.py

def func_py_caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

def test_caesar_cipher():
    text = "Hello, World!"
    shift = 3
    print(f"Original: {text}")
    print(f"Encrypted: {func_py_caesar_cipher(text, shift)}")

if __name__ == "__main__":
    test_caesar_cipher()
