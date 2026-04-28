from collections import deque
import sys

n, m = map(int, input().split())

# create adjacency list of m edges between n nodes
adj = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

# 0 if unassigned, 1 or 2 for two different teams
team = [0] * (n + 1)

def bfs(start):
    q = deque([(start)])
    team[start] = 1

    while q:
        node = q.popleft()
        for neighbor in adj[node]:
            # if unvisited 
            if team[neighbor] == 0:
                # assign friend opposite team
                team[neighbor] = 3 - team[node]
                q.append(neighbor)
            # if visited and same team, not bipartite
            elif team[neighbor] == team[node]:
                return False
    return True  

# check each component
for node in range(1, n + 1):
    if team[node] == 0:
        if not bfs(node):
            print("IMPOSSIBLE")
            sys.exit()

print(*team[1:])