import sys
import heapq

def dijkstra(n, adj):
    INF = 10**18
    dist = [INF] * (n + 1)
    dist[1] = 0

    pq = [(0, 1)]  # (distance, node)

    while pq:
        current_dist, u = heapq.heappop(pq)

        # Skip outdated entries
        if current_dist > dist[u]:
            continue

        for v, w in adj[u]:
            if dist[v] > current_dist + w:
                dist[v] = current_dist + w
                heapq.heappush(pq, (dist[v], v))

    return dist[1:]  # exclude index 0


def main():
    input = sys.stdin.read
    data = input().split()

    n, m = map(int, data[:2])
    index = 2

    adj = [[] for _ in range(n + 1)]

    for _ in range(m):
        a = int(data[index])
        b = int(data[index + 1])
        c = int(data[index + 2])
        index += 3
        adj[a].append((b, c))

    result = dijkstra(n, adj)
    print(*result)


if __name__ == "__main__":
    main()