from collections import deque


def BFS(start, end):
    visited[start] = True
    q = deque()
    q.append(start)
    parent = [-1] * (n + 1)

    while q:
        v = q.popleft()

        if v == end:
            break

        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
                parent[i] = v

    if not visited[end]:
        return None

    path = []
    current = end
    while current != -1:
        path.append(current)
        current = parent[current]
    path.reverse()
    return path


n, m = map(int, input().split())
start = 1
end = n
graph = {}
for i in range(1, n + 1):
    graph[i] = []
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [False] * (n + 1)
path = BFS(start, end)
if path is None:
    print("IMPOSSIBLE")
else:
    print(len(path))
    print(*path)