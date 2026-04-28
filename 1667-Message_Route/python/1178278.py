n,m = map(int, input().split())

adj = [[] for i in range(n)]

for _ in range(m):
 a, b = map(int, input().split())
 a-=1; b-=1
 adj[a].append(b); adj[b].append(a)
dist = [float('inf')]*n
dist[0]=1
used = [False]*n
used[0]=True
queue = [0]
parent = [-1]*n
while(queue):
 top = queue.pop(0)
 for to in adj[top]:
  if (not used[to]):
   used[to]=True
   queue.append(to)
   dist[to]=dist[top]+1
   parent[to]=top
if (not used[n-1]):
 print("IMPOSSIBLE")
else:
 print(dist[n-1])
 cur = n-1
 path =[]
 while(cur!=-1):
  path.append(cur+1)
  cur = parent[cur]
 print(*path[::-1])