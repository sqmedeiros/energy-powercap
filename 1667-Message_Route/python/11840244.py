from collections import deque, defaultdict

n, m = map(int, input().split())
edges = []
dist = [-1] * (n + 1)
dist[1] = 0
queue = deque([1])
parent = [-1] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    edges.append((a, b))

adj = defaultdict(list)

for a, b in edges:
    adj[a].append(b)
    adj[b].append(a)

while queue:
    node = queue.popleft()

    for neighbour in adj[node]:
        if dist[neighbour] == -1:
            dist[neighbour] = dist[node] + 1
            parent[neighbour] = node
            queue.append(neighbour)
            if neighbour == n:
                path = []
                cur = n
                while cur != -1:
                    path.append(cur)
                    cur = parent[cur]
                path.reverse()

                print(len(path))
                print(*path)
                exit()
else:
    print("IMPOSSIBLE")