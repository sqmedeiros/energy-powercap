n, m = [int(j) for j in input().split()]

def fill(G, i, visited):
    remaining = {i}
    while remaining:
        node = remaining.pop()
        visited.add(node)
        for edge in G[node]:
            if edge not in visited:
                remaining.add(edge)

def get_base_cities(G):
    representative_cities = []
    visited = set()
    for i in range(1, n + 1):
        if i in visited:
            continue

        representative_cities.append(i)
        fill(G, i, visited)

    return representative_cities

# Create a graph with n nodes
G = {}
for i in range(1, n + 1):
    G[i] = []

# Add edges to the graph
for i in range(m):
    a, b = [int(j) for j in input().split()]
    G[a].append(b)
    G[b].append(a)

# Get the connected components
cities = get_base_cities(G)

# Print the number of roads needed
print(len(cities) - 1)

# Connect components to each other
for i in range(1, len(cities)):
    print(cities[i], cities[i - 1])