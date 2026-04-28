import heapq
def my_custome_dijkastra(n,edges_with_time_delay):
    dist =[float('inf')]*(n+1)
    visited = [False]*(n+1)
    dist[1]=0
    dist[0]=0

    q = []
    heapq.heappush(q,(0,1))

    while q:
        just_to_stor_dis_of_u_temporarily,u = heapq.heappop(q)

        if visited[u]:continue

        visited[u]=True

        for c, time_delay in edges_with_time_delay[u]:
            if dist[c]>dist[u]+time_delay:
                dist[c]= dist[u]+time_delay
                heapq.heappush(q,(dist[c],c))
    return dist[1:]
n,m = map(int,input().split())

edges_with_time_delay = [[] for i in range(n+1)]

for i in range(m):
    u,v,time_delay = map(int,input().split())
    edges_with_time_delay[u].append((v,time_delay))

result = my_custome_dijkastra(n,edges_with_time_delay)
print(*result)