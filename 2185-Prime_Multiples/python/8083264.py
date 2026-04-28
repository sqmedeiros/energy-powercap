import math
import sys

r = sys.stdin
w = sys.stdout

n, k = map(int, input().split())
a = list(map(int, input().split()))

res = 0
for bm in range(1, 1 << k):
    prod = 1
    sgn = 0
    for i in range(k):
        if ((bm & (1 << i)) != 0):
            prod *= a[i]
            sgn += 1
    res += (1 if sgn % 2 == 1 else -1) * (n//prod)

print(res)