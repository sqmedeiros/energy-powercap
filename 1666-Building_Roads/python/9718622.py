from collections import defaultdict, deque

def find_connected_components(n, edges):
    # Create an adjacency list
    adj_list = defaultdict(list)
    for a, b in edges:
        adj_list[a].append(b)
        adj_list[b].append(a)

    # To keep track of visited cities
    visited = [False] * (n + 1)
    components = []

    def bfs(start):
        queue = deque([start])
        visited[start] = True
        component = []
        while queue:
            node = queue.popleft()
            component.append(node)
            for neighbor in adj_list[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
        return component

    # Find all components
    for city in range(1, n + 1):
        if not visited[city]:
            component = bfs(city)
            components.append(component)

    return components

def min_roads_to_connect_all_cities(n, m, edges):
    components = find_connected_components(n, edges)
    k = len(components) - 1

    # If only one component, no roads are needed
    if k == 0:
        return 0, []

    new_roads = []
    # To connect the components, we can simply connect each consecutive component
    for i in range(len(components) - 1):
        new_roads.append((components[i][0], components[i + 1][0]))

    return k, new_roads

# Reading input
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Getting the result
k, new_roads = min_roads_to_connect_all_cities(n, m, edges)

# Output the result
print(k)
for road in new_roads:
    print(road[0], road[1])