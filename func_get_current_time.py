# func_get_current_time.py
from datetime import datetime

def func_get_current_time():
    return datetime.now().time()

print(func_get_current_time())
