import sys
sys.setrecursionlimit(10**5)
n, r = map(int, input().split())
adj = [[] for _ in range(n)]

# Build adjacency list
for _ in range(r):
    r1, r2 = map(int, input().split())
    adj[r1-1].append(r2-1)
    adj[r2-1].append(r1-1)

visited = [False] * n
connected_comps = 0
representatives = []  # To store one node from each connected component

def dfs(node):
    visited[node] = True
    for neighbor in adj[node]:
        if not visited[neighbor]:
            dfs(neighbor)

# Count connected components and store their representatives
for node in range(n):
    if not visited[node]:
        representatives.append(node)  # Save this node as a representative
        dfs(node)
        connected_comps += 1

# Number of new roads required
new_roads = connected_comps - 1
print(new_roads)

# Print the roads to be added
for i in range(1, len(representatives)):
    print(representatives[i-1] + 1, representatives[i] + 1)  # Convert back to 1-indexed