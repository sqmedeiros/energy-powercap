import heapq

def main():
    n, m = map(int, input().split())
    distancia = [float('inf')] * (n + 1)
    distancia[1] = 0
    visitados = [False] * (n + 1)
    grafo = [[] for _ in range(n + 1)]

    for _ in range(m):
        u, v, w = map(int, input().split())
        grafo[u].append((v, w))

    queue = [(0, 1)]

    while queue:
        distancia_atual, no_atual = heapq.heappop(queue)
        if visitados[no_atual]:
            continue
        visitados[no_atual] = True

        for vizinho, peso in grafo[no_atual]:
            distancia_vizinho = distancia_atual + peso

            if distancia[vizinho] > distancia_vizinho:
                distancia[vizinho] = distancia_vizinho
                heapq.heappush(queue, (distancia[vizinho], vizinho))
            else:
                continue

    print(*distancia[1:])

main()