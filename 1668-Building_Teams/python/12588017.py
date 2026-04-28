
from collections import deque

def bfs(s):
    q=deque()
    q.append(s)
    t[s-1]=1
    while q:
        u = q.popleft()
        for v in graph[u]:
            if t[v-1] ==0:
                t[v-1]=3-t[u-1] 
                q.append(v)
            elif t[v-1]==t[u-1]:
                print("IMPOSSIBLE")
                exit(0)

n,m=map(int,input().split())
graph={i:[] for i in range(1,n +1)}
for i in range(m):
    u, v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

t=[0]*n
for i in range(1,n+1):
    if t[i-1]==0:
        bfs(i)

print(*t)