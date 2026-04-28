import sys
sys.setrecursionlimit(10**6)

def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())

    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)

    visited = [False] * (n + 1)
    components = []

    def dfs(u, comp):
        visited[u] = True
        comp.append(u)
        for v in adj[u]:
            if not visited[v]:
                dfs(v, comp)

    # Pronađi sve komponente
    for i in range(1, n + 1):
        if not visited[i]:
            comp = []
            dfs(i, comp)
            components.append(comp)

    # Minimalan broj cesta
    k = len(components) - 1
    print(k)

    # Spoji komponente "u lanac"
    for i in range(len(components) - 1):
        print(components[i][0], components[i+1][0])

if __name__ == "__main__":
    main()