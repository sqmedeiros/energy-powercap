import sys
sys.setrecursionlimit(10**6)

def dfs(node, parent):
    size = 1
    for child in graph[node]:
        if child != parent:
            size += dfs(child, node)
    subordinates[node] = size - 1
    return size

# Read input
n = int(input())
graph = [[] for _ in range(n + 1)]
subordinates = [0] * (n + 1)

# Build the graph
bosses = list(map(int, input().split()))
for i, boss in enumerate(bosses, start=2):
    graph[boss].append(i)
    graph[i].append(boss)

# Perform DFS starting from the general director (node 1)
dfs(1, 0)

# Print results
print(*subordinates[1:])