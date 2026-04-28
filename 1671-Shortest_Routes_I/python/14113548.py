from functools import *
from itertools import *
from collections import *
from math import *
from bisect import *
from heapq import *
from sys import stdin, stdout

m, n = map(int, input().split())
g = defaultdict(list)
for x in range(n):
    u,v,w = map(int, input().split())
    g[u].append((v,w))

path = [inf]*(m+1)
heap = []
heappush(heap, (0,1))
while heap:
    d,u = heappop(heap)
    if path[u]>d:
        path[u] = d
        for v,w in g[u]:
            if path[v]>d+w:
                heappush(heap, (d+w, v))
print(*path[1:])

