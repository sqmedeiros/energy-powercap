import fileinput
import sys


def is_solved(l, r, i, j, target):
    if l == i or r == i or l == j or r == j:
        return False
    if a_s[l][0] + a_s[r][0] == target:
        return True
    return False


data = [x.strip() for x in fileinput.input()]
n, x = [int(x) for x in data[0].split()]
a_s = [int(x) for x in data[1].split()]
# a_s = [(int(x), i + 1) for i, x in enumerate(data[1].split())]
# a_s = sorted(a_s)

cache = {}
for i in range(n):
    # Check if a_s[i] + a_s[j] is a solution using cached values
    for j in range(i + 1, n):
        target = x - a_s[i] - a_s[j]
        if target in cache:
            print(f"{i+1} {j+1} {cache[target][0]} {cache[target][1]}")
            sys.exit(0)

    # cache all possible values
    for j in range(i):
        v = a_s[i] + a_s[j]
        cache[v] = (i+1, j+1)

print("IMPOSSIBLE")