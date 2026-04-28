import sys
from collections import deque

def bfs(vi, vf):
    distance[vi] = 1
    came_from[vi] = vi
    q = deque()
    q.append(vi)
    while q:
        node = q.popleft()

        for child in graph[node]:
            if not visited[child]:
                q.append(child)
                came_from[child] = node
                distance[child] = distance[node] + 1
                visited[child] = True
                if child == vf: return True
    return False


n, m = [int(i) for i in sys.stdin.readline().split()]

graph = [[] for _ in range(n+1)]
distance = [float('inf') for _ in range(n+1)]
came_from = [0] * (n+1)
visited = [False] * (n+1)

n_has_conection = False
for _ in range(m):
    a, b = [int(i) for i in sys.stdin.readline().split()]
    graph[a].append(b)
    graph[b].append(a)
    if not n_has_conection and (a == n or b == n): n_has_conection = True

if n_has_conection and bfs(1, n):
    print(distance[n])

    trip = deque()
    trip.appendleft(n)
    node = n
    while came_from[node] != 1:
        trip.appendleft(came_from[node])
        node = came_from[node]
    trip.appendleft(1)

    print(' '.join(map(str, trip)))
else:
    print('IMPOSSIBLE')
