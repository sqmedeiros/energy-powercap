from collections import deque
n, m = map(int, input().split())

adj = [[] for _ in range(n + 1)]

for _ in range(m):
    v, u = map(int, input().split())
    adj[v].append(u)
    adj[u].append(v)


first, last = 1, n

visited = [0] * (n + 1)
pred = [-1] * (n + 1)
dist = [-1] * (n + 1)
q = deque()
visited[first] = 1
q.append(first)
dist[first] = 0
#  q = [a1, a2, a3, a4, a5] q.popleft() = a1
while q:
    v = q.popleft()
    for u in adj[v]:
        if visited[u] == 0:
            visited[u] = 1
            pred[u] = v
            dist[u] = dist[v] + 1
            q.append(u)
        if u == last:
            q = deque()

#  pred
if dist[last] != -1:
    print(dist[last] + 1)
    n = last
    path = [last]
    while n != first:
        n = pred[n]
        path.append(n)

    print(*path[::-1])
else:
    print('IMPOSSIBLE')