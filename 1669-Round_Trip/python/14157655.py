from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(2000000)

n,m=map(int,input().split())

graph=[[]for _ in range(n+1)]

for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited=[False]*(n+1)

parent=[-1]*(n+1)
cycle=[]

def dfs(u,p):
    visited[u]=True
    for v in graph[u]:
        if v==p:
            continue
        if not visited[v]:
            parent[v]=u
            if dfs(v,u):
                return True
        else:
            cycle.append(v)
            x=u
            while x!=v:
                cycle.append(x)
                x=parent[x]
            cycle.append(v)
            cycle.reverse()
            return True
    return False

found = False
for i in range(1, n+1):
    if not visited[i]:
        if dfs(i, -1):
            found = True
            break

if not found:
    print("IMPOSSIBLE")
else:
    print(len(cycle))
    print(*cycle)


