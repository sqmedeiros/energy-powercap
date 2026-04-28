from collections import defaultdict, deque

def find_minimum_roads(n, m, roads):
    graph = defaultdict(list)

    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)

    visited = [False] * (n + 1)
    components = []

    def bfs(node):
        queue = deque([node])
        visited[node] = True
        component = []
        while queue:
            curr = queue.popleft()
            component.append(curr)
            for neighbor in graph[curr]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
        return component

    for city in range(1, n + 1):
        if not visited[city]:
            components.append(bfs(city))

    k = len(components) - 1
    new_roads = []
    for i in range(len(components) - 1):
        new_roads.append((components[i][0], components[i + 1][0]))

    return k, new_roads

n, m = map(int, input().split())
roads = [tuple(map(int, input().split())) for _ in range(m)]
k, new_roads = find_minimum_roads(n, m, roads)
print(k)
for road in new_roads:
    print(road[0], road[1])