import sys
from collections import deque

sys.setrecursionlimit(200000)

def BFS(v):
    queue = deque([v])
    visitado[v] = True
    while queue:
        nodo = queue.popleft()
        for u in grafo[nodo]:
            if not visitado[u]:
                visitado[u] = True
                queue.append(u)

# Entrada
input = sys.stdin.read
data = input().split()

# Lectura de n y m
n, m = map(int, data[:2])

# Construcción del grafo con listas de adyacencia
grafo = [[] for _ in range(n + 1)]
index = 2
for _ in range(m):
    u, v = int(data[index]), int(data[index + 1])
    grafo[u].append(v)
    grafo[v].append(u)
    index += 2

visitado = [False] * (n + 1)
nodos_representantes = []

for ciudad in range(1, n + 1):
    if not visitado[ciudad]:
        nodos_representantes.append(ciudad)
        BFS(ciudad)

# Construcción de carreteras mínimas
k = len(nodos_representantes) - 1
print(k)
for i in range(k):
    print(nodos_representantes[i], nodos_representantes[i + 1])