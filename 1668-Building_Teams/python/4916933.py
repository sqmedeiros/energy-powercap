import sys
sys.setrecursionlimit(10**9)
input = lambda: sys.stdin.readline().strip("\r\n")
from collections import defaultdict, deque

n, m = map(int, input().split())
adj = defaultdict(list)
for _ in range(m):
    u, v = map(lambda x: int(x)-1,input().split())
    adj[u].append(v)
    adj[v].append(u)
col = [-1]*n
res = True
for i in range(n):
    if col[i] == -1:
        q = deque([(i,0)])
        col[i] = 0
        while q:
            v, c = q.popleft()
            for j in adj[v]:
                if col[j] == c: res = False
                if col[j] == -1: 
                    col[j] = c^1
                    q.append((j,col[j]))

if res:
    for i in col:
        if i: print(2,end=" ")
        else: print(1, end=" ")
else: print("IMPOSSIBLE")