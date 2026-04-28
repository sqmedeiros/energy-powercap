from math import inf
from sys import stdin


def solve():
    stdin.readline()
    A = [int(x) for x in stdin.readline().split()]

    cur, res = 0, -inf

    for a in A:
        cur = max(a, cur + a)
        res = max(res, cur)

    print(res)


solve()