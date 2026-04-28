from collections import deque
n, m = map(int, input().split())
graph = {}
for i in range(1, n + 1):
    graph[i] = []

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(start, end):
    visited = set()
    parent = {}
    queue = deque([start])
    visited.add(start)

    while queue:
        curr = queue.popleft()
        if curr == end:
            break
        for neighbor in graph[curr]:
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = curr
                queue.append(neighbor)

    if end not in visited:
        print("IMPOSSIBLE")
        return

    path = []
    node = end
    while node != start:
        path.append(node)
        node = parent[node]
    path.append(start)
    path.reverse()
    print(len(path))
    print(*path)

bfs(1, n)