import sys

from collections import defaultdict
from collections import deque
sys.setrecursionlimit(10**5)


def dfs(adj,visited,prev,node,check):
    stack=[]
    stack.append(node)
    while stack:
        front=stack.pop()
        visited[front]=1
        for child in adj[front]:
            if visited[child]==0:
                prev[child]=front
                stack.append(child)
            else:
                end=front
                start=child
                path=[]
                path.append(start)
                path.append(end)
                while end!=start and end!=-1:
                    end=prev[end]
                    path.append(end)
                if path[len(path)-1]!=-1 and len(path)>3:
                    print(len(path))
                    print(*path)
                    check[0]=True
                    return 





n,m=map(int,input().split())
adj=defaultdict(list)
for _ in range(m):
    u,v=map(int,input().split())

    adj[u].append(v)
    adj[v].append(u)
prev=[0]*(n+1)
visited=[0]*(n+1)
check=[False]
for i in range(1,n+1):
    if visited[i]==0:
        dfs(adj,visited,prev,i,check)
    if check[0]:
        break
if check[0]==False:
    print("IMPOSSIBLE")







