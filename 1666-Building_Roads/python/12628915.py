from collections import deque
n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)
visited = [False] * (n + 1)
road = []
for i in range(1, n + 1):
    if not visited[i]:
        road.append(i)
        q = deque([i])
        visited[i] = True
        while q:
            cur = q.popleft()
            for neighbor in adj[cur]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    q.append(neighbor)
print(len(road) - 1)
for i in range(len(road) - 1):
    print(road[i], road[i + 1])