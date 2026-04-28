from collections import deque

n, m = map(int, input().split())
adj = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

color = [0] * (n+1)  # 0 = unvisited, 1 = team1, 2 = team2

def bfs(start):
    queue = deque([start])
    color[start] = 1
    while queue:
        node = queue.popleft()
        for neigh in adj[node]:
            if color[neigh] == 0:
                color[neigh] = 3 - color[node]  # alternate teams
                queue.append(neigh)
            elif color[neigh] == color[node]:
                return False  # not bipartite
    return True

possible = True
for i in range(1, n+1):
    if color[i] == 0:
        if not bfs(i):
            possible = False
            break

if not possible:
    print("IMPOSSIBLE")
else:
    print(" ".join(map(str, color[1:])))