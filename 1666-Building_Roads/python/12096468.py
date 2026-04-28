import sys
from collections import deque

def bfs(start, graph, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

def build_roads(n, m, roads):
    graph = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)

    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)

    components = []
    for city in range(1, n + 1):
        if not visited[city]:
            components.append(city)
            bfs(city, graph, visited)

    num_new_roads = len(components) - 1
    new_roads = [(components[i], components[i+1]) for i in range(num_new_roads)]

    return num_new_roads, new_roads

# Entrada de datos optimizada
input_data = sys.stdin.read().splitlines()
n, m = map(int, input_data[0].split())
roads = [tuple(map(int, line.split())) for line in input_data[1:m+1]]

num_new_roads, new_roads = build_roads(n, m, roads)
print(num_new_roads)
for road in new_roads:
    print(*road)