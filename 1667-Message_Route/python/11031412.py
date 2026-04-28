from collections import deque, defaultdict

def message_route(n, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    queue = deque([1])
    visited = [-1] * (n + 1)
    visited[1] = 0
    parent = [-1] * (n + 1)

    while queue:
        node = queue.popleft()
        if node == n:
            path = []
            while node != -1:
                path.append(node)
                node = parent[node]
            return len(path), list(reversed(path))
        for neighbor in graph[node]:
            if visited[neighbor] == -1:
                visited[neighbor] = visited[node] + 1
                parent[neighbor] = node
                queue.append(neighbor)

    return -1, []

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
length, path = message_route(n, edges)

if length == -1:
    print("IMPOSSIBLE")
else:
    print(length)
    print(" ".join(map(str, path)))