import sys
from collections import Counter, defaultdict, deque
from itertools import accumulate, combinations, permutations
from heapq import heappop, heappush
from math import inf
sys.setrecursionlimit(10**6)
MOD = 10**9 + 7

stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().rstrip()  # ignore trailing spaces

n = ni()
P = [0] + [p-1 for p in na()]
indegree = [0]*n
for i,p in enumerate(P):
    P[i] = p
    indegree[p] += 1

q = [a for a in range(n) if indegree[a] == 0]
ts = []
while q:
    a = q.pop()
    ts.append(a)
    b = P[a]
    indegree[b] -= 1
    if indegree[b] == 0:
        q.append(b)

subordinates = [0]*n
for a in ts:
    b = P[a]
    subordinates[b] += subordinates[a]+1
print(*subordinates)