from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    v, e = map(int, input().split())
    graph[v].append(e)
    graph[e].append(v)


visited = [False for _ in range(n + 1)]
parent = [0 for _ in range(n + 1)]
queue = deque([1])
visited[1] = True


while queue:
    curr = queue.popleft()
    if curr == n:  
        break
    for nb in graph[curr]:
        if not visited[nb]:
            queue.append(nb)
            visited[nb] = True
            parent[nb] = curr

if parent[n] == 0:
    print("IMPOSSIBLE")
else:
    path = []
    at = n
    while at != 0:
        path.append(at)
        at = parent[at]
    path.reverse()
    print(len(path))
    print(" ".join(map(str, path)))