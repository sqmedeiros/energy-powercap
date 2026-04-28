from collections import deque

# Read input
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
queue = deque([1])
visited = [False] * (n + 1)
parent = [-1] * (n + 1)
visited[1] = True

while queue:
    node = queue.popleft()
    for neighbor in graph[node]:
        if not visited[neighbor]:
            visited[neighbor] = True
            parent[neighbor] = node
            queue.append(neighbor)
if not visited[n]:
    print("IMPOSSIBLE")
else:
    path = []
    current = n
    while current != -1:
        path.append(current)
        current = parent[current]
    path.reverse()
    print(len(path))
    print(*path)