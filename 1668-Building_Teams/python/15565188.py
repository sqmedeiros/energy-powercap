import sys 
from collections import deque 
input = sys.stdin.readline 

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

color = [-1] * n
def bfs(start):
    queue = deque([start])
    color[start] = 0

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if color[neighbor] == -1:
                color[neighbor] = 1 - color[node]
                queue.append(neighbor)
            elif color[neighbor] == color[node]:
                return False
    return True

is_bipartite = True
for i in range(n):
    if color[i] == -1:
        if not bfs(i):
            is_bipartite = False
            break

if not is_bipartite:
    print("IMPOSSIBLE")
else:   
    result = [str(c + 1) for c in color]
    print(" ".join(result))