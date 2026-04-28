import sys

try:
    sys.stdin = open("input.txt", "r")
    sys.stdout = open("output.txt", "w")
except FileNotFoundError:
    pass

import math
from collections import Counter
from collections import defaultdict as dd, deque
from bisect import bisect_left as bl , bisect_right as br
from heapq import heappush, heappop
from math import gcd, floor, ceil, log2, sqrt , isqrt
from functools import lru_cache
from itertools import groupby as gb

#from sortedcontainers import SortedList, SortedSet,SortedDict


sys.setrecursionlimit(1000000)

MOD = 10**9 + 7

N = 10**6 + 5
sieve = [1] * (N)
sieve[0] = sieve[1] = 0
fac = [1 for i in range(N)]
ifac = [1 for i in range(N)]
primes = []

def soe():
    for i in range(2, N):
        if sieve[i] == 1:  
            for j in range(i*i, N, i):
                sieve[j] = 0

    for i in range(N):
        if sieve[i]:
            primes.append(i)

def compute_factorials():
    for i in range(1, N):
        fac[i] = fac[i-1] * i % MOD


    ifac[-1] = pow(fac[-1], MOD - 2, MOD) 

    for i in range(N-2, -1, -1):
        ifac[i] = ifac[i+1] * (i+1) % MOD

def factorize(x):
    factors = []
    while x != 1:
        factors.append(spf[x])
        x //= spf[x]
    return factors

def is_prime(x):
    return x > 1 and sieve[x] == 0

def comb(n , r):
    return fac[n] * ifac[r] % MOD * ifac[n - r] % MOD

def perm(n  ,r):
    return fac[n] * ifac[n - r] % MOD


input = sys.stdin.readline

take_int = lambda: int(input())
take_line = lambda: map(int, input().split())
take_list = lambda: list(map(int, input().split()))
take_string = lambda: list(input().strip().split())
print_list = lambda x: print(*x)


def solve(): 

    n , m = take_line()

    comp = n
    par = [i for i in range(n)]
    def find(x):
        if x == par[x]:
            return x

        par[x] = find(par[x])
        return par[x]

    def unite(a , b):
        nonlocal comp
        pa , pb = find(a) , find(b)
        if pa != pb:
            par[pa] = pb
            comp -= 1

    for _ in range(m):
        u , v = take_line()
        u -= 1
        v -= 1
        unite(u , v)

    if comp == 1:
        print(0)
        return

    ans = []
    prev = comp
    for i in range(0 , n - 1):
        unite(i , i + 1)

        if comp < prev:
            if comp == 1:
                ans.append((i , i + 1))
                break
            else:
                ans.append((i , i + 1))
                prev = comp
        else:
            prev = comp


    print(len(ans))
    for u , v in ans:
        print(u + 1 , v + 1)





solve()

# t = take_int()
# for _ in range(t):
#     solve()
