from collections import deque

def is_bipartite(n, edges):
    graph = [[] for _ in range(n + 1)]
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    color = [-1] * (n + 1)  # -1: unvisited, 0 or 1: teams

    for start in range(1, n + 1):
        if color[start] == -1:
            queue = deque([start])
            color[start] = 0

            while queue:
                u = queue.popleft()
                for v in graph[u]:
                    if color[v] == -1:
                        color[v] = 1 - color[u]
                        queue.append(v)
                    elif color[v] == color[u]:
                        return False, []  # Not bipartite
    return True, color

# Input reading
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

ok, color = is_bipartite(n, edges)
if not ok:
    print("IMPOSSIBLE")
else:
    # Output the team of each student
    print(' '.join(str(c + 1) for c in color[1:]))  # team numbers: 1 or 2