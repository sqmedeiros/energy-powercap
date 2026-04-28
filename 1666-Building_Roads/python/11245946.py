def find_roads():
    n, m = map(int, input().split())

    parent = list(range(n + 1))
    rank = [0] * (n + 1)

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        px = find(x)
        py = find(y)

        if px == py:
            return

        if rank[px] < rank[py]:
            px, py = py, px

        parent[py] = px
        if rank[px] == rank[py]:
            rank[px] += 1

    for _ in range(m):
        a, b = map(int, input().split())
        union(a, b)

    components = set()
    for i in range(1, n + 1):
        components.add(find(i))

    components = list(components)
    required = len(components) - 1
    print(required)

    for i in range(required):
        print(components[i], components[i + 1])

find_roads()