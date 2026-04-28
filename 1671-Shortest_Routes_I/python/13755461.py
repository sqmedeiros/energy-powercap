import heapq

def dijkstra(grafo, inicio):
    n = len(grafo)
    distancias = [float('inf')] * n
    distancias[inicio] = 0
    visitado = [False] * n
    cola = [(0, inicio)]

    while cola:
        distActual, nodo = heapq.heappop(cola)
        if visitado[nodo]:
            continue
        visitado[nodo] = True

        for vecino, peso in grafo[nodo]:
            if distancias[nodo] + peso < distancias[vecino]:
                distancias[vecino] = distancias[nodo] + peso
                heapq.heappush(cola, (distancias[vecino], vecino))

    return distancias

def main():
    n, m = map(int, input().split())
    grafo = [[] for _ in range(n + 1)]

    for i in range(m):
        u, v, w = map(int, input().split())
        grafo[u].append((v, w))  

    distancias = dijkstra(grafo, 1)
    print(*distancias[1:])  

main()