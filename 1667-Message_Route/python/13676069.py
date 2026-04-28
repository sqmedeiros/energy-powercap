from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1) # False: unvisited
parent = [-1] * (n + 1)

def bfs(start, end):
    queue = deque([start])
    visited[start] = True

    while queue:
        u = queue.popleft()
        if u == end:
            return True
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                queue.append(v)
    return False


found = bfs(1, n)

if not found:
    print("IMPOSSIBLE")
else:
    # backtracking for path
    path = []
    current = n
    while current != -1:
        path.append(current)
        current = parent[current]
    path.reverse()

    print(len(path))
    print(*path)