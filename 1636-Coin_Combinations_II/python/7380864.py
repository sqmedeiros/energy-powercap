from collections import *
from itertools import permutations
import sys, math
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]
def err(*s): print(*s, file=sys.stderr)


def solve(n, x, c):
    dp = [0 for _ in range(x + 1)]
    dp[0] = 1
    for i in range(n):
        for j in range(x):
            if j + c[i] <= x:
                dp[j + c[i]] += dp[j]
                dp[j + c[i]] %= 10**9 + 7

    return dp[x]


def main():
    n, x = nl()
    c = nl()
    print(solve(n, x, c))


if __name__ == '__main__':
    main()