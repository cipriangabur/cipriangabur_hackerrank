# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict


def find_indices(list_to_check, item_to_find):
    indices = []
    for idx, value in enumerate(list_to_check):
        if value == item_to_find:
            indices.append(idx)
    return indices if len(indices) else [-2]


d = defaultdict(list)
inp = input().split()
n, m = int(inp[0]), int(inp[1])
for i in range(n + m):
    d['A' if i < n else 'B'].append(input())
for elem in d['B']:
    print(" ".join(str(el + 1) for el in find_indices(d['A'], elem)))
