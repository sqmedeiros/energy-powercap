def find_connected_components(n, adj):
    visited = [False] * (n + 1)
    representatives = []

    def dfs(node):
        stack = [node]
        while stack:
            cur = stack.pop()
            if not visited[cur]:
                visited[cur] = True
                for neighbor in adj[cur]:
                    if not visited[neighbor]:
                        stack.append(neighbor)

    for city in range(1, n + 1):
        if not visited[city]:
            representatives.append(city)
            dfs(city)

    return representatives

# Read n (cities) and m (roads)
n, m = map(int, input().split())
adj = {i: [] for i in range(1, n+1)}
for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

# Get the representatives for each component
representatives = find_connected_components(n, adj)

# The number of roads to add is the number of components minus one
k = len(representatives) - 1
print(k)
for i in range(k):
    print(representatives[i], representatives[i+1])