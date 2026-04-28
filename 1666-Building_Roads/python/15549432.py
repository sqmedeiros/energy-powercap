import sys, random, bisect, math
from collections import deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import permutations

input = lambda: sys.stdin.readline().rstrip()
mi = lambda: map(int, input().split())
li = lambda: list(mi())
ii = lambda: int(input())

def solve():
    n,m=mi()
    adj=defaultdict(list)
    for i in range(m):
        ui,vi=mi()
        adj[ui].append(vi)
        adj[vi].append(ui)
    vis=[0]*(n+1)
    def bfs(el):
        q=deque([el])
        while q:
            u=q.popleft()
            for v in adj[u]:
                if not vis[v]:
                    q.append(v)
                    vis[v]=1
    l=[]
    for i in range(1,n+1):
        if not vis[i]:
            vis[i]=1
            l.append(i)
            bfs(i)
    print(len(l)-1)
    for i in range(1,len(l)):
        print(l[i-1],l[i])



for _ in range(1):
    solve()