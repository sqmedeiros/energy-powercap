def find(parent, i):
    if parent[i] == i:
        return i
    else:
        root = find(parent, parent[i])
        parent[i] = root
        return root

def union(parent, rank, x, y):
    rootX = find(parent, x)
    rootY = find(parent, y)

    if rootX != rootY:
        if rank[rootX] < rank[rootY]:
            parent[rootX] = rootY
        elif rank[rootX] > rank[rootY]:
            parent[rootY] = rootX
        else:
            parent[rootY] = rootX
            rank[rootX] += 1

def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    n = int(data[0])
    m = int(data[1])

    edges = []
    index = 2
    for _ in range(m):
        a = int(data[index]) - 1
        b = int(data[index+1]) - 1
        edges.append((a, b))
        index += 2

    parent = list(range(n))
    rank = [0] * n

    for a, b in edges:
        union(parent, rank, a, b)

    components = {}
    for city in range(n):
        root = find(parent, city)
        if root not in components:
            components[root] = []
        components[root].append(city)

    component_roots = list(components.keys())
    k = len(component_roots) - 1

    print(k)
    if k > 0:
        roads_to_add = []
        for i in range(1, len(component_roots)):
            u = components[component_roots[i - 1]][0] + 1
            v = components[component_roots[i]][0] + 1
            roads_to_add.append((u, v))

        for road in roads_to_add:
            print(road[0], road[1])

main()
