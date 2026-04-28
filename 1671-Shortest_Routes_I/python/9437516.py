import heapq

MAXD = 10**17

def dijkstra(n, graph):
    dist = [MAXD] * (n + 1)
    dist[1] = 0
    pq = [(0, 1)]  # (distance, node)
    while pq:
        d, u = heapq.heappop(pq)
        if dist[u] < d:
            continue
        for v, c in graph[u]:
            if dist[v] <= c + d:
                continue
            dist[v] = c + d
            heapq.heappush(pq, (dist[v], v))
    return dist

def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    n = int(data[0])
    m = int(data[1])

    graph = [[] for _ in range(n + 1)]
    index = 2
    for _ in range(m):
        u = int(data[index])
        v = int(data[index + 1])
        c = int(data[index + 2])
        graph[u].append((v, c))
        index += 3

    dist = dijkstra(n, graph)
    print(' '.join(map(str, dist[1:])))

if __name__ == "__main__":
    main()