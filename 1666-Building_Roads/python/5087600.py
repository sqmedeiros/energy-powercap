import sys, io, os
from collections import defaultdict as dd, deque
# sys.setrecursionlimit(10**5)
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
# input = sys.stdin.readline
INF = float('inf')
MOD = 10**9 + 7

n, m = map(int, input().split())
adj = dd(list)
for _ in range(m):
    u,v = map(int, input().split())
    u-=1;v-=1
    adj[u].append(v)
    adj[v].append(u)

# def dfs(u):
    # for v in adj[u]:
        # if not vis[v]:
            # vis[v] = 1
            # dfs(v)

vis = [0]*n
cs = []
for i in range(n):
    if not vis[i]: 
        vis[i] = 1
        cs.append(i+1)
        q = [i]
        while q:
            j = q.pop()
            for k in adj[j]:
                if not vis[k]:
                    vis[k] = 1
                    q.append(k)

print(len(cs)-1)
for i in range(len(cs)-1):
    print(cs[i],cs[i+1])

