# DO NOT EDIT THIS
import functools
import math
import sys

input = sys.stdin.readline
from collections import deque, defaultdict
import heapq
import bisect
def counter(a):
    c = defaultdict(lambda : 0) # way faster than Counter
    for el in a:
        c[el] += 1
    return c

def inp(): return [int(k) for k in input().split()]
def si(): return int(input())
def st(): return input()

mxi = 10**10
mod = 10**9 + 7

# DO NOT EDIT ABOVE THIS

a, b = st(), st()
n1, n2 = len(a), len(b)
dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]

for i in range(len(dp) - 1, -1, -1):
    for j in range(len(dp[i]) - 1, -1, -1):
        if i == n1:
            dp[i][j] = n2 - j
        elif j == n2:
            dp[i][j] = n1 - i
        else:
            ins = dp[i + 1][j] + 1
            de = dp[i][j + 1] + 1
            rep = dp[i + 1][j + 1] + (1 if a[i] != b[j] else 0)
            dp[i][j] = min(ins, de, rep)

print(dp[0][0])
