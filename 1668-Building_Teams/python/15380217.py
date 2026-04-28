from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

color = [0] * (n + 1)

def bfs(start):
    queue = deque([start])
    color[start] = 1

    while queue:
        u = queue.popleft()

        for v in graph[u]:
            if color[v] == 0:
                color[v] = 3 - color[u]
                queue.append(v)
            elif color[v] == color[u]:
                return False

    return True

possible = True
for i in range(1, n + 1):
    if color[i] == 0:
        if not bfs(i):
            possible = False
            break

if possible:
    print(' '.join(map(str, color[1:n+1])))
else:
    print("IMPOSSIBLE")