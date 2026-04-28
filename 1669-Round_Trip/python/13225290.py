import sys
sys.setrecursionlimit(10**7)

# Read input
n, m = map(int, sys.stdin.readline().split())
adj = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    adj[u].append(v)
    adj[v].append(u)

visited = [0] * (n + 1)  # 0 = unvisited, 1 = visiting, 2 = visited
parent = [0] * (n + 1)

# Reconstruct the cycle when a back-edge u -> v is found
def build_cycle(u, v):
    path = [v]
    x = u
    # walk up from u to v using parent pointers
    while x != v:
        path.append(x)
        x = parent[x]
    path.append(v)
    path.reverse()
    return path

# DFS to detect a cycle
def dfs(u):
    visited[u] = 1
    for v in adj[u]:
        if visited[v] == 0:
            parent[v] = u
            cycle = dfs(v)
            if cycle:
                return cycle
        elif visited[v] == 1 and v != parent[u]:
            # Found a back-edge to an ancestor: cycle detected
            return build_cycle(u, v)
    visited[u] = 2
    return None

# Try DFS from every component
for i in range(1, n + 1):
    if visited[i] == 0:
        cycle = dfs(i)
        if cycle:
            print(len(cycle))
            print(*cycle)
            sys.exit(0)

# If no cycle found
print("IMPOSSIBLE")