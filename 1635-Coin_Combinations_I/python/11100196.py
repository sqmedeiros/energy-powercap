import sys
from collections import Counter, defaultdict, deque
from itertools import accumulate, combinations, permutations
from heapq import heappop, heappush
from math import inf
sys.setrecursionlimit(10**6)
MOD = 10**9 + 7

stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().rstrip()  # ignore trailing spaces

n,x = na()
C = na()
C.sort()
dp = [0]*(x+1)
dp[0] = 1
for i in range(x+1):
    for c in C:
        if i+c > x: break
        dp[i+c] += dp[i]
        dp[i+c] %= MOD
print(dp[x] % MOD)