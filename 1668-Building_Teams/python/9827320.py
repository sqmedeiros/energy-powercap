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
from collections import defaultdict as dd, deque as dq, Counter as Ct, OrderedDict
#from math import gcd,log,log2,log10
#from bisect import bisect_left, bisect_right
#from typing import List, Tuple
#from functools import lru_cache, cmp_to_key

def IO(name = ''):
    if name:
        sys.stdin = open(name+'.INP', 'r')
        sys.stdout = open(name+'.OUT', 'w')

def input(): return sys.stdin.readline()
#def input(): return sys.stdin.buffer.readline()

def print(x): return sys.stdout.write(x)

# sys.setrecursionlimit(int(1e6))

IO('')

# Constant
INF = float('inf')
maxn = int(1e5)+1
visited = [0] * maxn
graph = dd(list)
ans = [0]*(maxn)

def main() -> None:
    #Code
    n,m = map(int, input().split())
    edges = []
    for _ in range(m):
        u,v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
        edges.append((u,v))

    for i in range(1,n+1):
        if not visited[i]:
            BFS(i)

    for u,v in edges:
        if ans[u] == ans[v]:
            return print("IMPOSSIBLE")

    print(" ".join(map(str, ans[1:n+1])))

def BFS(source):
    q = [source]
    visited[source] = 1
    ans[source]=1
    while q:
        node = q.pop(0)

        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = 1
                ans[neighbor] = 3-ans[node]
                q.append(neighbor)

if __name__ == '__main__':
    main()