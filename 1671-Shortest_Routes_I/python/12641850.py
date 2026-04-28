import heapq as hp

def dijkstra():
    visited = [False] * (n+1)
    q = [(0,1)]
    dists[1] = 0

    while q:
        curr_w, curr_v = hp.heappop(q)
        if visited[curr_v]:
            continue
        visited[curr_v] = True

        for w, v in adj[curr_v]:
            new_w = curr_w + w
            if not visited[v] and new_w < dists[v]:
                hp.heappush(q, (new_w, v))
                dists[v] = new_w



n, m = [int(x) for x in input().split()]

adj = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = [int(x) for x in input().split()]
    adj[a].append((c, b))
    #adj[b].append((c, a))

dists = [float('inf')] * (n+1)

dijkstra()
for i in range(1, n+1):
    print(dists[i], end=' ')