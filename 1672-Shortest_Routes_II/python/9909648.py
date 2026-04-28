# for index, value in enumerate(list)
# '{:02d}'.format(1) --> 001
# '{0:.2f}'.format(1.5) --> 1.50
# Stack is DFS, Queue is BFS
# AND --> &, OR --> |, XOR --> ^
# (a/b)%c = (a mod (b * c) / b) mod c
# (a/b)%c = (a mod c * b^(c-2) mod c) mod c ||| c is prime number
# To use custom compare in heapq, make a Class have a __lt__ func

import sys
#from heapq import heapify, heappush, heappop
#from collections import defaultdict as dd, deque as dq, Counter as Ct, OrderedDict
#from math import gcd,log,log2,log10
#from bisect import bisect_left, bisect_right
#from typing import List, Tuple
#from functools import lru_cache, cmp_to_key

def IO(name = ''):
    if name:
        sys.stdin = open(name+'.INP', 'r')
        sys.stdout = open(name+'.OUT', 'w')

#def input(): return sys.stdin.readline()
def input(): return sys.stdin.buffer.readline()
print = sys.stdout.write
# sys.setrecursionlimit(int(1e6))

IO('')

# Constant
INF = 1<<40
maxn = 500
W = [INF] * (maxn**2)

def main() -> None:
    #Code
    n,m,q = map(int, input().split())
    for _ in range(m):
        u,v,w = map(int, input().split())
        u-=1
        v-=1
        if w < W[u+500*v]:
            W[u+500*v] = w
            W[v+500*u] = w

    floyd(n)
    for _ in range(q):
        a,b = map(int, input().split())
        a-=1
        b-=1
        if a==b: print('0')
        else: print(str(W[a+500*b]) if W[a+500*b] != INF else '-1')
        print("\n")

def floyd(n):
    for k in range(n):
        for u in range(n):
            if k == u or W[u+500*k] == INF: continue
            for v in range(u):
                if W[u+500*v] > W[u+500*k] + W[k+500*v]:
                    W[u+500*v] = W[v+500*u] = W[u+500*k] + W[k+500*v]

if __name__ == '__main__':
    main()