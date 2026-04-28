import heapq
n,m = [int(x) for x in input().split()]
inf = 100000000000001
adj = [[] for i in range(n+1)]

for i in range(m):
    a,b,c = [int(x) for x in input().split()]
    adj[a].append((b,c))

queue = [(0,1)]
ans = [inf for i in range(n+1)]
ans[1] = 0
while queue:
    dis, pos = heapq.heappop(queue)
    if ans[pos] < dis: continue
    for npos,s in adj[pos]:
        newdis = dis + s
        if newdis < ans[npos]:
            ans[npos] = newdis
            heapq.heappush(queue, (newdis,npos))

print(*ans[1:])