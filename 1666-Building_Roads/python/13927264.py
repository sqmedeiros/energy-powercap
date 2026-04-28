from collections import deque

n, m = map(int, input().split())
edges = []
for _ in range(m):
    edges.append(list(map(int, input().split())))

adj = [[] for _ in range(n+1)]
for x, y in edges:
    adj[x].append(y)
    adj[y].append(x)

visited = [0 for _ in range(n+1)]


def bfs(node):
    q = deque([node])
    while q:
        node = q.popleft()
        visited[node] = 1
        for nex in adj[node]:
            if visited[nex] == 0:
                q.append(nex)


roads = []
for i in range(1,n+1):
    if visited[i] == 0:
        roads.append(i)
        bfs(i)

res = []
for i in range(len(roads)-1):
    res.append(roads[i:i+2])

print(len(res))
for x, y in res:
    print(x, y)