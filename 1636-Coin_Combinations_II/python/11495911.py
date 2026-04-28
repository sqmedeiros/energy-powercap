import sys
sint = lambda: sys.stdin.readline().rstrip("\r\n")
nint = lambda: int(input())
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))
INF = float('inf')
from functools import lru_cache
from itertools import groupby, accumulate
from bisect import bisect_right
M = 10**9 + 7
from collections import Counter


def solve(n, x, C):
    dp = [0]*(x+1)
    dp[0] = 1

    for i in range(n):
        for j in range(C[i], x + 1):
            dp[j] += dp[j - C[i]]
            dp[j] %= M

    return dp[x]%M




if __name__ == "__main__":
    t = 1 #nint()
    for _ in range(t):
        n, x = mint()
        C = lint()
        ans = solve(n, x, C)
        print(ans)