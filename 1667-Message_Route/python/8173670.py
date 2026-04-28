from collections import deque

n, m = map(int, input().split())
grafo = {i: [] for i in range(1, n + 1)}

for _ in range(m):
    a, b = map(int, input().split())
    grafo[a].append(b)
    grafo[b].append(a)

visitado = [False] * (n + 1)
pai = [-1] * (n + 1)

fila = deque([1])
visitado[1] = True

while fila:
    atual = fila.popleft()

    for vizinho in grafo[atual]:
        if not visitado[vizinho]:
            visitado[vizinho] = True
            pai[vizinho] = atual
            fila.append(vizinho)

if not visitado[n]:
    print("IMPOSSIBLE")
else:
    rota = []
    v = n
    while v != -1:
        rota.append(v)
        v = pai[v]

    rota.reverse()
    print(len(rota))
    print(*rota)