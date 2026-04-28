# https://cses.fi/problemset/task/1668

import sys

n, m = [int(s) for s in sys.stdin.readline().split()]
graph = {}
for _ in range(m):
    source, dest = [int(s) for s in sys.stdin.readline().split()]
    if source not in graph:
        graph[source] = []
    if dest not in graph:
        graph[dest] = []
    graph[source].append(dest)
    graph[dest].append(source)

for i in range(1, n + 1):
    if i not in graph:
        graph[i] = []


def dfs(graph, root, visited):
    stack = [(root, 1)]  # (node, component)
    while stack:
        node, component = stack.pop()
        visited[node] = component
        for neighbour in graph[node]:
            if not visited[neighbour]:
                stack.append((neighbour, 3 - component))
            elif visited[neighbour] == component:  # cycle inside component
                return False
    return True


visited = [0] * (n + 1)
for node in graph:
    if not visited[node]:
        if not dfs(graph, node, visited):
            print("IMPOSSIBLE")
            break
else:
    print(" ".join(str(v) for i, v in enumerate(visited) if i > 0))