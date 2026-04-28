from collections import defaultdict, deque
I = lambda : map(int, input().split())

n, m = I()
adj = defaultdict(list)

for _ in range(m):
    a, b = I()
    adj[a].append(b)
    adj[b].append(a)

vis = [False] * (n + 1)
q = deque([1])
dist = {}
dist[1] = (0, 0)
vis[1] = True


while q:
    # print(q)
    u = q.popleft()
    d, _ = dist[u]
    for v in adj[u]:
        if not vis[v]:
            vis[v] = True
            dist[v] = (d + 1, u)
            q.append(v)

        if v == n: 
            print(dist[v][0] + 1)
            path = [v]
            while True:
                path.append(dist[v][1])
                v = dist[v][1]
                if v == 1: break
            path = path[::-1]
            print(*path)
            q = []
            exit()


print("IMPOSSIBLE")