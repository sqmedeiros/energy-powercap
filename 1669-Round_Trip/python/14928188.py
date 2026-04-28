from collections import defaultdict

def find_cycle(n, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = [False] * (n + 1)
    parent = [-1] * (n + 1)
    cycle = []

    for start in range(1, n + 1):
        if visited[start]:
            continue

        stack = [(start, -1)]
        while stack:
            u, par = stack.pop()
            if visited[u]:

                continue
            visited[u] = True
            parent[u] = par
            for v in graph[u]:
                if not visited[v]:
                    stack.append((v, u))
                elif v != par and not cycle:
                    cycle.append(v)
                    x = u
                    while x != v:
                        cycle.append(x)
                        x = parent[x]
                    cycle.append(v)
                    cycle.reverse()
                    print(len(cycle))
                    print(*cycle)
                    return

    print("IMPOSSIBLE")


n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

find_cycle(n, edges)