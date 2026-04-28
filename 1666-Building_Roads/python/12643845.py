import sys
from collections import deque

sys.setrecursionlimit(10**6)

def addLista(lista, de, para):
    lista[de].append(para)
    lista[para].append(de)  # Adiciona a aresta bidirecional

def dfs_iterativa(no, listaAdj, visitados, componente):
    stack = deque([no])  # Inicializa a pilha com o nó inicial
    visitados[no] = True  # Marca o nó inicial como visitado
    while stack:  # Enquanto houver nós na pilha
        atual = stack.pop()  # Remove o nó do topo da pilha
        componente.append(atual)  # Adiciona o nó atual ao componente
        for vizinho in listaAdj[atual]:  # Itera sobre os vizinhos do nó atual
            if not visitados[vizinho]:  # Se o vizinho ainda não foi visitado
                visitados[vizinho] = True  # Marca o vizinho como visitado
                stack.append(vizinho)  # Adiciona o vizinho à pilha

if __name__ == "__main__":
    # Lê o número de cidades (V) e estradas (E)
    V, E = map(int, input().split())
    listaAdj = [[] for _ in range(V)]
    visitados = [False] * V
    componentes = []  # Lista para armazenar todos os componentes

    # Lê as estradas e constrói a lista de adjacência
    for _ in range(E):
        de, para = map(int, input().split())
        addLista(listaAdj, de - 1, para - 1)

    # Encontra todos os componentes conectados
    for i in range(V):
        if not visitados[i]:
            componente = []  # Lista para armazenar os nós do componente atual
            dfs_iterativa(i, listaAdj, visitados, componente)
            componentes.append(componente)  # Adiciona o componente à lista de componentes

    # Calcula as estradas necessárias para unir os componentes
    k = len(componentes) - 1
    print(k)
    for i in range(len(componentes) - 1):
        # Conecta o primeiro nó de um componente ao primeiro nó do próximo
        print(f"{componentes[i][0] + 1} {componentes[i + 1][0] + 1}")