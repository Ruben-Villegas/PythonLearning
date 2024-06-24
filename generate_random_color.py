# generate_random_color.py
import random

def random_color():
    return f'#{random.randint(0, 0xFFFFFF):06x}'

if __name__ == "__main__":
    print(f"Random color code: {random_color()}")
