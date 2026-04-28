# Source: https://usaco.guide/general/io
import heapq

n, m = map(int, input().split())
arr = [[] for i in range(n + 1)]
for i in range(m):
    u, v, peso = map(int, input().split())
    arr[u].append((v, peso))

def dijkstra(grafo, inicio, final):
    dist = [-1] * (n + 1)

    pq = [] 
    heapq.heappush(pq, (0, inicio))

    while pq:
        pesoActual, nodo = heapq.heappop(pq)
        if dist[nodo] != -1:
            continue

        dist[nodo] = pesoActual

        for hijo in grafo[nodo]:
            vecino, peso = hijo
            nuevo = pesoActual + peso
            if dist[vecino] == -1 or nuevo < dist[vecino]:
                heapq.heappush(pq, (nuevo, vecino))

    return dist


res = dijkstra(arr, 1, n)
print(*res[1:])

#print(arr)