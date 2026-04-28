n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    graph[a].append(b)
    graph[b].append(a)


def is_bipartite(graph):
    n = len(graph)
    color = [-1] * n

    for start in range(n):
        if color[start] == -1:
            color[start] = 0
            stack = [start]

            while stack:
                parent = stack.pop()

                for child in graph[parent]:
                    if color[child] == -1:
                        color[child] = 1 - color[parent]
                        stack.append(child)
                    elif color[parent] == color[child]:
                        return False, color

    return True, color


flag, color = is_bipartite(graph)
if flag:
    print(*map(lambda x: x + 1, color))
else:
    print("IMPOSSIBLE")