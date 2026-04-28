from collections import defaultdict
import heapq

n,m=map(int, input().split())
adj=defaultdict(list)


for i in range(m):
    a, b, c = map(int, input().split())
    adj[a].append((b, c))

distances={node: float("inf") for node in range(1,n+1)}
distances[1]=0 
q=[(0,1)]

while q:
    dist,node=heapq.heappop(q)
    if dist>distances[node]:
        continue
    for neig,w in adj[node]:
        newD=dist+w
        if newD<distances[neig]:
            distances[neig]=newD
            heapq.heappush(q,(newD,neig))

dada=[]
for i in range(1,n+1):
    dada.append(str(distances[i]))
print(" ".join(dada))