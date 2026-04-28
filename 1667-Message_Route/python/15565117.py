import sys 
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u - 1].append(v - 1)
    graph[v - 1].append(u - 1)

parent = [-1] * n
visited = [False] * n
q = deque([0])
visited[0] = True
flag = False
while q:
    node = q.popleft()
    if node == n - 1:
        flag = True
        break
    for neighbor in graph[node]:
        if not visited[neighbor]:
            visited[neighbor] = True
            parent[neighbor] = node
            q.append(neighbor)

if not flag:
    print("IMPOSSIBLE")
else:
    path = []
    curr = n - 1
    while curr != -1:
        path.append(curr + 1)
        curr = parent[curr]
    path.reverse()
    print(len(path))
    print(' '.join(map(str, path)))