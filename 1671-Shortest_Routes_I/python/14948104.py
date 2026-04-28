import sys
import heapq

input = sys.stdin.readline  # leitura rápida

def main():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))

    INF = 10**18
    dist = [INF] * (n + 1)
    dist[1] = 0

    pq = [(0, 1)]  # (distância, nó)

    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            if dist[v] > d + w:
                dist[v] = d + w
                heapq.heappush(pq, (dist[v], v))

    print(*dist[1:])

if __name__ == "__main__":
    main()