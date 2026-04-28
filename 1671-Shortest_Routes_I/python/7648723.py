import heapq
def dk(n,adj,start): 
    dist = [float('inf')]*n
    dist[start]=0
    pq=[]
    heapq.heappush(pq,(0,start))
    while pq: 
        d,u=heapq.heappop(pq)
        if d > dist[u]:
            continue 
        for v,w in adj[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq,(dist[v],v))

    return dist

g,h = map(int,input().split())
a= [[] for _ in range (g)]
for i in range (h): 
    x,y,z = map(int, input().split())
    a[x - 1].append((y-1, z))
dists=dk(g,a,0) 
print(*dists)