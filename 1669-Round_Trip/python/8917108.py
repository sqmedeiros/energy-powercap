import sys
sys.setrecursionlimit(3*10**7)

def construir_grafo(n, m):
    adjacencias = {}
    for i in range(m):
        cidade_a, cidade_b = map(int, input().split())
        if cidade_a not in adjacencias:
            adjacencias[cidade_a] = []
        if cidade_b not in adjacencias:
            adjacencias[cidade_b] = []
        adjacencias[cidade_a].append(cidade_b)
        adjacencias[cidade_b].append(cidade_a)

    for cidade in range(1, n + 2):
        if cidade not in adjacencias:
            adjacencias[cidade] = []
    return adjacencias


def dfs(vertice, pai):

    visitados.add(vertice)
    caminho.append(vertice)

    while adjacencias[vertice]:
        vizinho = adjacencias[vertice].pop(0)

        if vizinho != pai:
            if vizinho not in visitados:
                if dfs(vizinho, vertice):
                    return True

            else:
                rota = []
                ultimo_no_caminho = caminho[-1]
                while ultimo_no_caminho != vizinho:
                    rota.append(caminho.pop())
                    ultimo_no_caminho = caminho[-1]
                rota.append(vizinho)
                rota.append(vertice)
                tamanho_rota = len(rota)
                print(tamanho_rota)
                for i in range(tamanho_rota):
                    print(rota[i], end=" ")
                print()
                return True
    caminho.pop()
    return False


num_cidades, num_estradas = map(int, input().split())
adjacencias = construir_grafo(num_cidades, num_estradas)
visitados = set()
caminho = []

cidade = 1
while cidade <= num_cidades:
    if cidade not in visitados and dfs(cidade, 0):
        break
    cidade += 1
else:
    print("IMPOSSIBLE")