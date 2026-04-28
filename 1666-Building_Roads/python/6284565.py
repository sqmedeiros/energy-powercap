from queue import Queue

def bfs(initial):
    q = Queue()
    q.put(initial)
    visited[initial] = True

    while not q.empty():
        vertex = q.get()

        for u in graph[vertex]:
            if not visited[u]:
                q.put(u)
                visited[u] = True

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)
components = []

for v in range(1, n + 1):
    if not visited[v]:
        components.append(v)
        bfs(v)

required_roads = len(components) - 1
print(required_roads)

for i in range(required_roads):
    if (i + 1 < len(components)):
        a = components[i]
        b = components[i + 1]
        print(a, b)