#@sorcerer_21
from collections import *
import sys,math
input = lambda:sys.stdin.readline().strip()
mapin = lambda:map(int,input().split())

n, k = mapin()
a = list(mapin())
res = 0

# inclusion-exclusion principle
for i in range(1, 1 << k):
    setbits = 0
    temp = n
    for j in range(k):
        if i & (1 << j):
            setbits += 1
            temp //= a[j]
    res += temp if setbits % 2 else -temp
print(res)