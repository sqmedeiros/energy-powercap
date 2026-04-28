# for index, value in enumerate(list)
# '{:02d}'.format(1) --> 001
# '{0:.2f}'.format(1.5) --> 1.50
# Stack is DFS, Queue is BFS
# AND --> &, OR --> |, XOR --> ^
# (a/b)%c = (a mod (b * c) / b) mod c
# (a/b)%c = (a mod c * b^(c-2) mod c) mod c ||| c is prime number
# To use custom compare in heapq, make a Class have a __lt__ func

import sys
from heapq import heapify, heappush, heappop
from collections import defaultdict as dd, deque as dq, Counter as Ct, OrderedDict
from math import gcd,log,log2,log10
from bisect import bisect_left, bisect_right
from typing import List, Tuple
from functools import lru_cache

def IO(name = ''):
    if name:
        sys.stdin = open(name+'.INP', 'r')
        sys.stdout = open(name+'.OUT', 'w')

input = sys.stdin.buffer.readline

IO('')

INF = int(1e9)
MOD = int(1e9) + 7

def main() -> None:
    #Code
    n,x = map(int, input().split())
    coins = sorted(list(map(int, input().split())))
    f = [0] * (1+x)
    f[0] = 1

    for coin in coins:
        for i in range(coin, x + 1):
            f[i] += f[i-coin]%MOD

    print(f[-1]%MOD)

if __name__ == '__main__':
    main()