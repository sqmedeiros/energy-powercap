from collections import deque


def find_path(graph, n):
    previous = [0] * (n+1)
    distance = [float('inf')] * (n+1)
    previous[1] = -1
    distance[1] = 0
    q = deque([1])
    while q:
        vertex = q.popleft()
        neighbors = graph[vertex]
        for neighbor in neighbors:
            if previous[neighbor] == 0 or distance[neighbor] > distance[vertex]+1:
                previous[neighbor] = vertex
                distance[neighbor] = distance[vertex]+1
                q.append(neighbor)
    if previous[n] == 0:
        return None
    path = []
    vertex = n
    while vertex != -1:
        path.append(vertex)
        vertex = previous[vertex]
    return path[::-1]


def message_route():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    path = find_path(graph, n)
    if path:
        print(len(path))
        print(*path)
    else:
        print('IMPOSSIBLE')


message_route()