# https://cses.fi/problemset/task/2166
 
import bisect, os, sys
from io import BytesIO, IOBase
from math import log2, ceil
 
sys.setrecursionlimit(10**6)
 
n, q = [int(s) for s in sys.stdin.readline().split()]
arr = [int(s) for s in sys.stdin.readline().split()]
 
 
n = 2 ** ceil(log2(n))
tree = [[0, 0] for _ in range(2 * n)]
 
 
def build():
    for i, a in enumerate(arr):
        tree[n + i] = [a, a if a > 0 else 0]
    a = n >> 1
    b = n
    while a:
        for i in range(a, b):
            # tree[i] = combine(tree[i << 1], tree[i << 1 | 1])
            tree[i][0] = tree[i << 1][0] + tree[i << 1 | 1][0]
            tree[i][1] = max(tree[i << 1][1], tree[i << 1][0] + tree[i << 1 | 1][1])
        a >>= 1
        b >>= 1
 
 
# data = [sum, max prefix]
def combine(left, right):
    if left is None:
        return right
    if right is None:
        return left
    max_prefix = max(left[1], left[0] + right[1])
    return [left[0] + right[0], max_prefix]
 
def update(k, x):
    k += n
    tree[k][0] = x
    tree[k][1] = x
    while k > 1:
        k >>= 1
        tree[k][0] = tree[2 * k][0] + tree[2 * k + 1][0]
        tree[k][1] = max(tree[2 * k][1], tree[2 * k][0] + tree[2 * k + 1][1])
        # tree[k] = combine(tree[2 * k], tree[2 * k + 1])
 
 
 
 
def query(a, b):
    a += n
    b += n
    x = [0, 0]  # sum, prefix sum
    y = [0, 0]
    while a <= b:
        if a & 1:
            x = [x[0] + tree[a][0], max(x[0] + tree[a][1], x[1])]
            a += 1
        if b % 2 == 0:
            y = [y[0] + tree[b][0], max(tree[b][1], tree[b][0] + y[1])]
            b -= 1
        a >>= 1
        b >>= 1
    return max(x[1], x[0] + y[1])
 
 
build()
 
ans = []
for _ in range(q):
    a, b, c = [int(s) for s in sys.stdin.readline().split()]
    if a == 1:
        update(b - 1, c)
    else:
        ans.append(query(b - 1, c - 1))
        
print('\n'.join((str(x) for x in ans)))