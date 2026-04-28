import heapq
from sys import stdin as si, stdout as so

n, m = map(int, si.readline().split())  # qtd de vértices / qtd de arestas

q = [(0, 1)]  # inicializa fila de prioridade
dist = [0 for i in range(n)]
#pai = {1: None}

# define pais e distâncias de cada vértice
for i in range(2, n+1):
    dist[i-1] = float("inf")
    #pai[i] = None

# lê e armazena as conecções
adjs = [[] for i in range(n)]
for i in range(m):
    a, b, c = map(int, si.readline().split())
    adjs[a-1].append((c, b))

# dijkstra
while q:
    d, v = heapq.heappop(q)  # remove o menor
    if d <= dist[v-1]:  # verifica se já encontramos um menor caminho
        for d1, v1 in adjs[v-1]:
            newd = dist[v-1] + d1
            if dist[v1-1] > newd:
                dist[v1-1] = newd
                #pai[v1] = v
                heapq.heappush(q, (newd, v1))
ans = " ".join(map(str, dist))
so.write(ans)