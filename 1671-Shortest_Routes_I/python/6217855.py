import sys
import queue

sys.setrecursionlimit(100000)


def dijkstra(x: int):
    q: queue.PriorityQueue = queue.PriorityQueue()
    dist[x] = 0
    q.put((0, x))

    while (not q.empty()):
        _, u = q.get()

        if (proc[u]):
            continue

        proc[u] = True

        for vw in adj[u]:
            v, w = vw
            if (dist[u] + w <= dist[v]):
                dist[v] = dist[u] + w
                q.put((dist[v], v))


n, m = map(int, input().split())

adj: list = []
for i in range(n):
    adj.append([])
INF = 10**18+7
proc: list = [False]*n
dist: list = [INF]*n

for i in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    adj[a].append((b, c))

dijkstra(0)

for i in range(n):
    print(dist[i], end=' ')