import sys
from collections import deque

sys.setrecursionlimit(10000000);

lista = {}
n, m = map(int, input().split())
for i in range(1,n+1):
    lista[i] = []

for i in range(m):
    v1, v2 = map(int, input().split())
    lista[v1].append(v2)
    lista[v2].append(v1)

uo, ma = 1, n
def wea(inicio, lista):
    visitados = set()
    parent  = {}
    queue = deque()

    queue.append(inicio)
    visitados.add(inicio)
    parent[inicio] = None

    while queue:
        actual = queue.popleft()

        for vecino in lista[actual]:
            if vecino not in visitados:
                queue.append(vecino)
                visitados.add(vecino)
                parent[vecino] = actual
    return parent

padres = wea(ma, lista)
if uo not in padres.keys():
    print('IMPOSSIBLE')
else:
    c = True
    camino = [uo]
    act = uo
    while c:
        if act is not None:
            act = padres[act]
            if act is not None:
                camino.append(act)

        if act is None:
            c = False
            print(len(camino))
            print(*camino)