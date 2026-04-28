#import resource
import sys

#resource.setrlimit(resource.RLIMIT_STACK, (2**29, -1))
sys.setrecursionlimit(10 ** 7)
from collections import deque


def read_graph():
    n, m = map(int, input().split())
    gr = [[] for _ in range(n)]
    for _ in range(m):
        a, b = [int(i) for i in input().split()]
        a -= 1
        b -= 1
        gr[a].append(b)
        gr[b].append(a)
    return gr


def Building_Teams():
    g = read_graph()
    n = len(g)
    ciclos = [False]
    t = [0]
    color = ['blanco'] * n
    num = [0] * n
    dad = [-1] * n
    start, end = [0], [0]

    def dfs(u):
        if ciclos[0]:
            return
        color[u] = 'gris'
        t[0] += 1
        num[u] = t[0]
        for vecino in g[u]:
            if color[vecino] == 'blanco':
                dfs(vecino)
            else:
                if color[vecino] == 'gris':
                    nciclo = abs(num[u] - num[vecino]) + 1
                    if nciclo > 2:
                        ciclos[0] = True

            if ciclos[0]:
                break
        color[u] = 'negro'
        t[0] -= 1
        return

    def dfs_iterative(u):
        s = [u]
        t[0] += 1
        num[u] = t[0]
        while len(s):
            if ciclos[0]:
                break
            nod = s.pop()
            color[nod] = "gris"

            for v in g[nod]:
                if color[v] != 'negro':
                    if color[v] == 'blanco':
                        s.append(v)
                        dad[v] = nod
                    num[v] = num[nod] + 1
                else:
                    nciclo = abs(num[nod] - num[v]) + 1
                    if nciclo > 2:
                        start[0], end[0] = v, nod
                        ciclos[0] = True

            color[nod] = 'negro'
        t[0] = 0
        return

    def reconstruction(ini, fin):
        ans = [ini+1]
        while fin != ini:
            ans.append(fin+1)
            fin = dad[fin]
        ans.append(ini+1)
        print(len(ans))
        [print(x, end=' ') for x in ans]
        return

    for node in range(n):
        if ciclos[0]:
            reconstruction(start[0], end[0])
            exit(0)
        if color[node] == 'blanco':
            dfs_iterative(node)

    print("IMPOSSIBLE")
    return


Building_Teams()