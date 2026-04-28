import sys
from collections import deque

input = sys.stdin.read
data = input().split()
n, m = int(data[0]), int(data[1])
edges = list(map(int, data[2:]))

g = [[] for _ in range(n + 1)]
for i in range(0, 2 * m, 2):
    u, v = edges[i], edges[i + 1]
    g[u].append(v)
    g[v].append(u)

team = [0] * (n + 1) 
def bfs(start):
    q = deque()
    q.append(start)
    team[start] = 1
    while q:
        u = q.popleft()
        for v in g[u]:
            if team[v] == 0:
                team[v] = 3 - team[u]
                q.append(v)
            elif team[v] == team[u]:
                return False
    return True

possible = True
for i in range(1, n + 1):
    if team[i] == 0:
        if not bfs(i):
            possible = False
            break

if not possible:
    print("IMPOSSIBLE")
else:
    print(' '.join(map(str, team[1:])))