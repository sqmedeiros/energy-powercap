import sys 
from collections import deque
sys.setrecursionlimit(1000000)
n,m = list(map(int, input().split(" ")))

adj = [[] for i in range(n)]
pv = [None for i in range(n)]
visited = [False for _ in range(n)]
ans = []
ans_found = False

for i in range(m):
    a,b = list(map(int, input().split(" ")))
    adj[a-1].append(b-1)
    adj[b-1].append(a-1)

#cycles detection
def dfs_detect_cycles(v, parent):
    global ans_found
    visited[v] = True
    pv[v] = parent
    for u in adj[v]:
        if ans_found:
            return
        if u == parent:
            continue
        if visited[u]:
            ans_found = True
            v_c = v
            ans.append(u)
            ans.append(v_c)
            while v^u:
                ans.append(pv[v])
                v = pv[v]
            print(len(ans))
            for j in range(len(ans)):
                print(ans[j] + 1, end=" ")
            return
        else:
            dfs_detect_cycles(u, v)

for i in range(n):
    if not visited[i]:
        dfs_detect_cycles(i, -1)

if not ans_found:
    print('IMPOSSIBLE')