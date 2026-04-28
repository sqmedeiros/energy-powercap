import heapq

n, m = map(int, input().split())

# grafo como lista de adyacencia
grafo = [[] for _ in range(n + 1)]

# Conexiones
for _ in range(m):
    a, b, c = map(int, input().split())
    grafo[a].append((b, c))

# Inicializar distancias con infinito
INF = 10**18
# La distancia a cada ciudad desde la ciudad 1
dist = [INF] * (n + 1)
dist[1] = 0

# Cola de prioridad para Dijkstra
cola = []
heapq.heappush(cola, (0, 1))  # (distancia, ciudad)

while cola:
    d, u = heapq.heappop(cola)
    if d > dist[u]:
        continue  # Ya hay un camino más corto
    for v, peso in grafo[u]:
        if dist[v] > dist[u] + peso:
            dist[v] = dist[u] + peso
            heapq.heappush(cola, (dist[v], v))

# Se imprimen las distancias desde la ciudad 1 a todas las ciudades
print(' '.join(str(dist[i]) for i in range(1, n + 1)))