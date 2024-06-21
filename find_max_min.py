# find_max_min.py
def find_max_min(numbers):
    max_num = max(numbers)
    min_num = min(numbers)
    return max_num, min_num

numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
max_num, min_num = find_max_min(numbers)
print(f"Numbers: {numbers}")
print(f"Max: {max_num}, Min: {min_num}")
  
