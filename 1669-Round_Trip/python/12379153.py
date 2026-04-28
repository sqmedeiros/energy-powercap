import sys
from collections import defaultdict

sys.setrecursionlimit(10**6)
input = sys.stdin.read

# Funções utilitárias para entrada e saída
def see():
    return map(int, sys.stdin.readline().split())

def put(*args):
    print(*args, end=" ")

def putl(*args):
    print(*args)

# Constantes
INF = float('inf')
PI = 3.141592653589793
MOD = 1000000007

# Grafo e variáveis auxiliares
adj = defaultdict(list)
vis = {}
cyc = []

def dfs(s, p):
    """ Realiza DFS para encontrar um ciclo em um grafo não direcionado """
    vis[s] = True
    for i in adj[s]:
        cyc.append(i)
        if i not in vis:
            if dfs(i, s):
                return True
        elif i != p:
            return True
        cyc.pop()
    return False

def solve():
    """ Resolve o problema principal """
    n, m = see()

    for _ in range(m):
        u, v = see()
        adj[u].append(v)
        adj[v].append(u)

    for i in range(1, n + 1):
        cyc.append(i)
        if i not in vis and dfs(i, -1):
            ans = [cyc[-1]]
            for j in reversed(cyc[:-1]):
                ans.append(j)
                if j == cyc[-1]:
                    break
            putl(len(ans))
            put(*ans)
            return
        cyc.pop()

    putl("IMPOSSIBLE")

if __name__ == "__main__":
    solve()