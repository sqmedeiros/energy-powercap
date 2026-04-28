import sys

sys.setrecursionlimit(2 * 10**5 + 5)

def solucao():
    n = int(sys.stdin.readline())

    if n==1:
        print(0)
        return

    chefes = list(map(int, sys.stdin.readline().split()))

    adj = [[] for _ in range(n+1)]

    for i, chefe in enumerate(chefes):
        funcionario_id = i+2
        adj[chefe].append(funcionario_id)

    sub_arvores_tamanho = [0] * (n+1)

    def dfs(u):
        tamanho = 1
        for v in adj[u]:
            tamanho += dfs(v)

        sub_arvores_tamanho[u] = tamanho
        return tamanho

    dfs(1)

    resultado = [sub_arvores_tamanho[i] - 1 for i in range(1, n+1)]

    print(*resultado)


solucao()