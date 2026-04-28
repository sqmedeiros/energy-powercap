#!/usr/bin/python3.7
from random import randint
import resource, sys
resource.setrlimit(resource.RLIMIT_STACK, (2**29, -1))
sys.setrecursionlimit(10**7)

import heapq as pq #priority queue

#nodos, aristas
n, m = map(int, input().split())
adj = [[] for _ in range(n)]
# como es un grafo con pesos, la lista de 
# adyacencia guarda pares (vertice, peso_arista)

for _ in range(m):
    a, b, c = map(int, input().split())
    #v_inicio, v_fin, peso_arista
    # resto 1 a los vertices para que esten en el rango
    # [0, n-1]
    a -= 1
    b -= 1
    adj[a].append((b, c)) 


def dijkstra(n: int, adj: list, start: int):
    vis = [False for _ in range(n)]
    dist = [float('inf') for _ in range(n)]
    q = [] # cola de prioridad
    dist[start] = 0

    # En nuestra cola vamos a llevar 
    # pares (w, v) = (weight, vertex) = (peso, vertice/nodo)
    # por qué no (v, w) -> las tuplas se ordenan 
    # lexicograficamente por defecto

    pq.heappush(q, (0, start)) 

    while len(q) > 0:
        _, v = pq.heappop(q)

        if vis[v]: 
            continue 

        vis[v] = True

        for e, w in adj[v]:
            if dist[v] + w < dist[e] and vis[e] == False:
                dist[e] = dist[v] + w
                pq.heappush(q, (dist[e], e))

    return dist

ans = dijkstra(n, adj, 0)
for x in ans:
    print(x, end=' ')

