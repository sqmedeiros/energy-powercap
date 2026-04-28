import sys
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
parent = [0] * (n+1)

# Build the graph
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

cycle_start = -1
cycle_end = -1

def dfs(v, par):
    global cycle_start, cycle_end
    visited[v] = True
    for neighbor in graph[v]:
        if neighbor == par:
            continue
        if visited[neighbor]:
            cycle_start = neighbor
            cycle_end = v
            return True
        parent[neighbor] = v
        if dfs(neighbor, v):
            return True
    return False

# Run DFS for every component
for i in range(1, n+1):
    if not visited[i]:
        if dfs(i, -1):
            break

if cycle_start == -1:
    print("IMPOSSIBLE")
else:
    path = [cycle_start]
    v = cycle_end
    while v != cycle_start:
        path.append(v)
        v = parent[v]
    path.append(cycle_start)
    path.reverse()
    print(len(path))
    print(' '.join(map(str, path)))