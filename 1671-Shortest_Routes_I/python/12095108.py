import sys
import heapq

def dijkstra(n, adj):
    INF = float('inf')
    dist = [INF] * (n + 1)
    dist[1] = 0
    pq = [(0, 1)]

    while pq:
        d, node = heapq.heappop(pq)
        if d > dist[node]:
            continue

        for neighbor, weight in adj[node]:
            new_dist = d + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))

    return dist[1:]

def main():
    input = sys.stdin.read
    data = input().split()

    index = 0
    n = int(data[index])
    m = int(data[index + 1])
    index += 2

    adj = [[] for _ in range(n + 1)]

    for _ in range(m):
        a = int(data[index])
        b = int(data[index + 1])
        w = int(data[index + 2])
        index += 3
        adj[a].append((b, w))

    result = dijkstra(n, adj)
    print(*result)

if __name__ == "__main__":
    main()