# Versão corrigida para o problema "Message Route"
# Corrige os problemas de KeyError quando não há caminho e melhora leitura/clareza.
import sys
from collections import deque

def bfs_shortest_path(adj, start, goal):
    """Retorna a lista de vértices do caminho mínimo start->goal (inclusive),
    ou None se goal não é alcançável."""
    q = deque([start])
    visited = set([start])
    parent = {start: None}

    while q:
        u = q.popleft()
        if u == goal:
            # alcançado; reconstruir caminho
            path = []
            cur = goal
            while cur is not None:
                path.append(cur)
                cur = parent[cur]
            path.reverse()
            return path

        for v in adj[u]:
            if v not in visited:
                visited.add(v)
                parent[v] = u
                q.append(v)

    # se chegar aqui, não alcançamos goal
    return None

def main():
    data = sys.stdin.readline().split()
    if not data:
        return
    n, m = map(int, data)  # n vértices, m arestas

    # criar lista de adjacência (1..n)
    adj = {i: [] for i in range(1, n+1)}

    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        adj[a].append(b)
        adj[b].append(a)

    path = bfs_shortest_path(adj, 1, n)
    if path is None:
        print("IMPOSSIBLE")
    else:
        print(len(path))
        print(' '.join(map(str, path)))

if __name__ == "__main__":
    main()