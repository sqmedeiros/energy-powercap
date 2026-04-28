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

n,m = na()
G = [[] for _ in range(n)]
for _ in range(m):
    a,b = na()
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)

team = [-1]*n
def dfs(s):
    if team[s] != -1: return
    team[s] = 1
    q = [s]
    while q:
        a = q.pop()
        for b in G[a]:
            if team[b] == -1:
                team[b] = 1-team[a]
                q.append(b)
            elif team[a] == team[b]:
                print("IMPOSSIBLE")
                exit()
for a in range(n):
    dfs(a)
print(*[t+1 for t in team])

