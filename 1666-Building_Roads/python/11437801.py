from collections import defaultdict

def find_connected_components(n, edges):
    # Create an adjacency list
    graph = defaultdict(list)
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    # Visited set to track visited nodes
    visited = [False] * (n + 1)

    def dfs(node, component):
        stack = [node]
        while stack:
            current = stack.pop()
            if not visited[current]:
                visited[current] = True
                component.append(current)
                for neighbor in graph[current]:
                    if not visited[neighbor]:
                        stack.append(neighbor)

    components = []

    # Find all connected components
    for i in range(1, n + 1):
        if not visited[i]:
            component = []
            dfs(i, component)
            components.append(component)

    return components

def minimum_new_roads(n, m, edges):
    # Find connected components
    components = find_connected_components(n, edges)
    num_components = len(components)

    # If there's only one connected component, no new roads are needed
    if num_components == 1:
        return 0, []

    # To connect k components, we need k-1 roads
    new_roads = []
    for i in range(num_components - 1):
        # Connect the first city of one component to the first city of the next
        new_roads.append((components[i][0], components[i + 1][0]))

    return num_components - 1, new_roads

# Input reading
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Solve the problem
k, roads = minimum_new_roads(n, m, edges)

# Output
print(k)
for road in roads:
    print(road[0], road[1])