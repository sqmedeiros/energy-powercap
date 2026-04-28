# Aaditya Upadhyay

from collections import *
from sys import stdin, stdout


def st(): return list(stdin.readline().strip())


def li(): return list(map(int, stdin.readline().split()))
def mp(): return map(int, stdin.readline().split())
def inp(): return int(stdin.readline())
def pr(n): return stdout.write(str(n)+"\n")


mod = 1000000007
INF = float('inf')


def solve():
    n, k = mp()
    l = li()
    dp = [INF for i in range(k+1)]
    dp[0] = 0
    l.sort()
    for i in range(1, k+1):
        for j in range(n):
            if i-l[j] >= 0:
                dp[i] = min(dp[i], 1+dp[i-l[j]])
            else:
                break
        if dp[-1] != INF:
            pr(dp[-1])
            return
    pr(-1)


for _ in range(1):
    solve()