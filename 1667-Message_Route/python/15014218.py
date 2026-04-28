from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())

    graph[a].append(b)
    graph[b].append(a)

visited = set()
queue = deque([1])
visited.add(1)
parent = [None] * (n + 1)
parent[1] = -1

while queue:
    current = queue.popleft()
    # print(current)

    for neighbor in graph[current]:
        if neighbor not in visited:
            queue.append(neighbor)
            visited.add(neighbor)
            parent[neighbor] = current
# print(parent)

if parent[n] != None:
    current = n
    path = []
    while current != -1:
        path.append(current)
        current = parent[current]
    print(len(path))
    print(" ".join(map(str, path[::-1])))
else:
    print("IMPOSSIBLE")