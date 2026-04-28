import sys
from collections import deque, defaultdict

sys.setrecursionlimit(10 ** 6)

MOD = 10 ** 9 + 7


def inplist(dtype):
    return [dtype(i) for i in input().split()]


def pow(a, b, mod):
    x = 1
    while b:
        if b & 1:
            x = (x * a) % mod
        a = (a * a) % mod
        b >>= 1
    return x


def debug(**kwargs):
    st = [f"{name}: {val}" for (name, val) in kwargs.items()]
    print(*st, sep=" | ")


import math

from collections import deque
import sys


def solve():
    n = int(input())
    arr = inplist(int)
    tree = defaultdict(list)
    for idx, val in enumerate(arr, 1):
        tree[val - 1].append(idx)
    ans = [0] * n

    def dfs(at, p=-1):
        curr = 0
        for to in tree[at]:
            if to == p:
                continue
            curr += 1 + dfs(to, p)
        ans[at] = curr
        return curr

    dfs(0)
    print(*ans, sep=" ")


def main():
    t = 1
    # t=int(input())
    for _ in range(t):
        solve()


if __name__ == "__main__":
    # sys.stdin = open("input.txt", "r")
    # sys.stdout = open("output.txt", "w")
    main()