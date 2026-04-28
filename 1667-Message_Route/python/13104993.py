from collections import deque
import sys
import heapq

n, m = map(int, input().split())  # first line input
adjlist = {i: [] for i in range(1, n + 1)}
visited = {i: -1 for i in range(1, n + 1)}
for _ in range(m):
    u, v = map(int, input().split())
    adjlist[u].append(v)
    adjlist[v].append(u)

queue = deque([1])
visited = {1: None}

while queue:
    node = queue.popleft()
    if node == n:  # Reached Maija's computer
        break
    for neighbor in adjlist[node]:
        if neighbor not in visited:
            visited[neighbor] = node
            queue.append(neighbor)
if n in visited:
    path = []
    curr = n
    while curr:
        path.append(curr)
        curr = visited[curr]
    path.reverse()
    print(len(path))
    s = [str(x) for x in path[0:]]
    print(" ".join(s))

else:
    print("IMPOSSIBLE")