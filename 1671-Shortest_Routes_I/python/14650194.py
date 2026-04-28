import sys
import heapq

def solve():
    input = sys.stdin.read
    data = list(map(int, input().split()))

    n, m = data[0], data[1]
    edges = data[2:]

    graph = [[] for _ in range(n+1)]

    for i in range(m):
        u, v, w = edges[i*3], edges[i*3+1], edges[i*3+2]
        graph[u].append((v, w))

    INF = 10**18
    dist = [INF] * (n+1)
    dist[1] = 0

    pq = []
    heapq.heappush(pq, (0, 1))  # (distance, node)

    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))

    print(' '.join(map(str, dist[1:])))

if __name__ == "__main__":
    solve()