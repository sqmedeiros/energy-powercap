from collections import defaultdict
import heapq

def dijkstra(num_vertices, num_arestas, arestas):
    grafo = defaultdict(list)
    for u, v, w in arestas:
        grafo[u].append((v, w))

    distancias = [float('inf')] * (num_vertices + 1)
    distancias[1] = 0
    fila_prioridade = [(0, 1)]

    while fila_prioridade:
        d, u = heapq.heappop(fila_prioridade)

        if d > distancias[u]:
            continue

        for v, w in grafo[u]:
            nova_distancia = d + w
            if nova_distancia < distancias[v]:
                distancias[v] = nova_distancia
                heapq.heappush(fila_prioridade, (nova_distancia, v))

    return distancias[1:]

num_vertices, num_arestas = map(int, input().split())
arestas = []
for _ in range(num_arestas):
    u, v, w = map(int, input().split())
    arestas.append((u, v, w))

distancias = dijkstra(num_vertices, num_arestas, arestas)
print(*distancias)