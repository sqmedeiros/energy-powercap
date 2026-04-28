import sys

sys.setrecursionlimit(10 ** 6)


def dfs(no, lista_adjacencia, resultado):
    cont = 0
    for node in lista_adjacencia[no]:
        cont += 1 + dfs(node, lista_adjacencia, resultado)
    resultado[no] = cont
    return cont


def calc_sub(n, lista_chefes):
    resultado = [0] * n
    dfs(0, lista_chefes, resultado)
    return resultado


n = int(input())
lista_chefes = [[] for _ in range(n)]

chefes = list(map(int, input().split()))
for i in range(1, n):
    chefe = chefes[i - 1] - 1
    lista_chefes[chefe].append(i)

print(*calc_sub(n, lista_chefes))