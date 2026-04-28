import sys
from collections import deque

def bfs(n,adj):
    li = deque()
    li.append(0)
    dist = [10**9 for _ in range(n)]
    dist[0] = 0
    vis = [ 0 for _ in range(n)]
    #print(li)
    while li:
        x = li.popleft()
        for i in adj[x]:
            if dist[i]>dist[x]+1:
                vis[i] = x
                dist[i] = dist[x]+1
                li.append(i)
    if dist[n-1]==10**9:
        print("IMPOSSIBLE")
    else:
        print(dist[n-1]+1)
        arr = []
        i = n-1
        while i!=0:
            arr.append(i+1)
            i = vis[i]
        arr.append(1)
        print(" ".join(map(str,arr[::-1])))

    #(dist)
    #return dist[n-1]

n,m = map(int,sys.stdin.readline().split())
adj = [[] for _ in range(n)]
for i in range(m):
    a,b = map(int,sys.stdin.readline().split())
    adj[a-1].append(b-1)
    adj[b-1].append(a-1)
bfs(n,adj)
#print(ans[0]+1)
#print(" ".join(map(str,ans[1][::-1])))