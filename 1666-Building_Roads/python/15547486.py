from collections import deque

def safe_input():
    line = input().strip()
    while line == "":
        line = input().strip()
    return line

n, m = map(int, safe_input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, safe_input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)
components = []

def bfs(start):
    q = deque([start])
    visited[start] = True
    while q:
        u = q.popleft()
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                q.append(v)

for i in range(1, n + 1):
    if not visited[i]:
        components.append(i)
        bfs(i)

k = len(components) - 1
print(k)
for i in range(k):
    print(components[i], components[i + 1])