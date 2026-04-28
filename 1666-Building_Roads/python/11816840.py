from collections import defaultdict, deque

def find_min_roads_to_connect(n, m, edges):
    graph = defaultdict(list)
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
    visited = [False] * (n + 1)
    components = []

    def bfs(start):
        queue = deque([start])
        component = []
        visited[start] = True
        while queue:
            node = queue.popleft()
            component.append(node)
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
        return component
    for i in range(1, n + 1):
        if not visited[i]:
            components.append(bfs(i))
    roads_to_add = []
    for i in range(1, len(components)):
        roads_to_add.append((components[i-1][0], components[i][0]))
    return len(roads_to_add), roads_to_add
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
k, roads = find_min_roads_to_connect(n, m, edges)
print(k)
for road in roads:
    print(road[0], road[1])