from collections import defaultdict, deque

def find_minimum_roads(n, m, edges):
    # Create an adjacency list
    graph = defaultdict(list)
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    # To find connected components
    visited = [False] * (n + 1)
    components = []

    def bfs(start):
        queue = deque([start])
        visited[start] = True
        component = []
        while queue:
            node = queue.popleft()
            component.append(node)
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
        return component

    # Find all connected components
    for i in range(1, n + 1):
        if not visited[i]:
            components.append(bfs(i))

    # Number of new roads required
    k = len(components) - 1

    # Create roads between representatives of components
    new_roads = []
    for i in range(1, len(components)):
        new_roads.append((components[i - 1][0], components[i][0]))

    return k, new_roads

# Input reading
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Find the solution
k, new_roads = find_minimum_roads(n, m, edges)

# Output the result
print(k)
for road in new_roads:
    print(road[0], road[1])