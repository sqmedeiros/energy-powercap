import sys
from collections import defaultdict, deque

def main():
    # Leer el número de ciudades (n) y caminos (m)
    n, m = map(int, sys.stdin.readline().split())

    # Crear un grafo usando una lista de adyacencia
    grafo = defaultdict(list)

    # Leer los caminos y construir el grafo
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        grafo[a].append(b)
        grafo[b].append(a)

    # Inicializar un arreglo para marcar ciudades visitadas
    visitado = [False] * (n + 1)

    # Lista para almacenar los componentes conectados
    componentes = []

    # Recorrer todas las ciudades para encontrar componentes conectados
    for ciudad in range(1, n + 1):
        if not visitado[ciudad]:
            # Usar BFS para encontrar todas las ciudades en este componente
            cola = deque()
            cola.append(ciudad)
            visitado[ciudad] = True
            componente = []

            while cola:
                nodo = cola.popleft()
                componente.append(nodo)

                # Explorar los vecinos de la ciudad actual
                for vecino in grafo[nodo]:
                    if not visitado[vecino]:
                        visitado[vecino] = True
                        cola.append(vecino)

            # Guardar el componente conectado
            componentes.append(componente)

    # El número de caminos nuevos necesarios es k-1, donde k es el número de componentes
    k = len(componentes)
    print(k - 1)

    # Construir los caminos nuevos conectando los componentes
    for i in range(1, k):
        print(componentes[i-1][0], componentes[i][0])

if __name__ == "__main__":
    main()