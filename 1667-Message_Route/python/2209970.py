import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
def I(): return input().strip()
def II(): return int(input().strip())
def LI(): return [*map(int, input().strip().split())]
import string, math, time, functools, random, fractions
from heapq import heappush, heappop, heapify
from bisect import bisect_left, bisect_right
from collections import deque, defaultdict, Counter, OrderedDict
from itertools import permutations, combinations, groupby
from operator import itemgetter


n, m = LI()
edges = defaultdict(lambda: set())
for i in range(m):
    left, right = LI()
    edges[left].add(right)
    edges[right].add(left)

visited = [False for i in range(n)]
parent = [None for i in range(n + 1)]


def bfs(x):
    que = deque()
    que.append(x)
    visited[x - 1] = True
    while que:
        pop = que.popleft()
        for vertex in edges[pop]:
            if visited[vertex - 1]:
                continue
            que.append(vertex)
            visited[vertex - 1] = True
            parent[vertex] = pop
            if vertex == n:
                return True
    return False


flag = bfs(1)
if not flag:
    print('IMPOSSIBLE')
else:
    ans = [n]
    base = n
    while True:
        if base == 1:
            break
        par = parent[base]
        ans.append(par)
        base = par
    print(len(ans))
    print(*ans[::-1])