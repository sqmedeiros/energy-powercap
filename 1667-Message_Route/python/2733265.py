from collections import defaultdict
from collections import deque
n,m=map(int,input().split())
graph=defaultdict(list)
for i in range(m):
 a,b=map(int,input().split())
 graph[a].append(b)
 graph[b].append(a)

prev={}
vis=[0]*(n+1)
q=deque()
q.append(1)
vis[1]=1
while q:
 x=q.popleft()
 if x in graph:
  for y in graph[x]:
   if vis[y]==0:
    prev[y]=x
    q.append(y)
    vis[y]=1

ex=n
res=[]
if n not in prev:
 print("IMPOSSIBLE")

else:
 while ex!=1:
  res.append(ex)
  ex=prev[ex]
 res.append(1)
 print(len(res))
 for i in range(len(res)-1,-1,-1):
  print(res[i], end=' ')



