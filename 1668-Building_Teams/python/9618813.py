import sys

from collections import defaultdict
from collections import deque
sys.setrecursionlimit(10**5)
def dfs(node,check):
    if teams[node]==0:
        teams[node]=1
    new_team=0
    if teams[node]==1:
        new_team=2
    else:
        new_team=1
    for child in adj[node]:
        if teams[child]==0:
            teams[child]=new_team
            dfs(child,check)
        else:
            if teams[child]!=new_team:
                check[0]=False
                return




n,m=map(int,input().split())
adj=defaultdict(list)
for _ in range(m):
    u,v=map(int,input().split())

    adj[u].append(v)
    adj[v].append(u)
teams=[0]*(n+1)
check=[True]
for i in range(1,n+1):
    if teams[i]==0:
        dfs(i,check)
    if check[0]==False:
        print("IMPOSSIBLE")
        break
if check[0]:

        print(*teams[1:])





