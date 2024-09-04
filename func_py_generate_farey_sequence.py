# func_py_generate_farey_sequence.py
def func_py_generate_farey_sequence(n):
    farey_seq = [(0, 1), (1, n)]
    for _ in range(2, n + 1):
        i = 1
        while i < len(farey_seq):
            a, b = farey_seq[i - 1]
            c, d = farey_seq[i]
            k = (n + b) // d
            farey_seq.insert(i, (k * c - a, k * d - b))
            i += 1
    return farey_seq

print(func_py_generate_farey_sequence(5))
