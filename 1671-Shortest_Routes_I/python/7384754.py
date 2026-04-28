import heapq

t = 1
# You can uncomment the line below and input the number of test cases interactively if needed.
# t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    adj = [[] for _ in range(n + 1)]
    dist = [float('inf')] * (n + 1)
    dist[1] = 0

    for _ in range(m):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))

    pq = [(0, 1)]
    heapq.heapify(pq)

    while pq:
        distance, node = heapq.heappop(pq)

        if distance > dist[node]:
            continue

        for child in adj[node]:
            if dist[child[0]] > distance + child[1]:
                dist[child[0]] = distance + child[1]
                heapq.heappush(pq, (distance + child[1], child[0]))

    for i in range(1, n + 1):
        print(dist[i], end=" ")