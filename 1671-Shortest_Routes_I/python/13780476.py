import sys
import heapq

def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())

    # Grafo dirigido con pesos
    adj = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        adj[a].append((b, c))

    # Distancias iniciales
    INF = 10**30
    dist = [INF] * (n+1)
    dist[1] = 0

    # Cola de prioridad para Dijkstra
    pq = [(0, 1)]  # (distancia acumulada, nodo)

    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in adj[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))

    # Imprimir distancias de 1 a n
    # (dist[1] = 0, luego las mínimas distancias a cada ciudad)
    print(' '.join(str(dist[i]) for i in range(1, n+1)))

if __name__ == "__main__":
    main()