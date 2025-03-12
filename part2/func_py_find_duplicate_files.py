# func_py_find_duplicate_files.py
import os
import hashlib

def func_py_find_duplicate_files(directory):
    hash_map = {}
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, "rb") as f:
                file_hash = hashlib.md5(f.read()).hexdigest()
            if file_hash in hash_map:
                print(f"Duplicate: {file_path} and {hash_map[file_hash]}")
            else:
                hash_map[file_hash] = file_path

func_py_find_duplicate_files("./test_folder")
