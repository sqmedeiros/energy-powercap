import sys
sys.setrecursionlimit(210000)  # A bit more than the maximum number of employees

import collections

n = int(input())
edges = [int(x) for x in input().split()]
graph = collections.defaultdict(list)

for direct_subordinates, boss in enumerate(edges, start=2):
    graph[boss].append(direct_subordinates)


subtree = [None] * (n + 1)
def dfs(vertix: int) -> int:
    count = 0

    for neighbor in graph[vertix]:
        count += dfs(neighbor) + 1

    subtree[vertix] = count
    return count

dfs(1)

for i in range(1, n + 1):
    print(subtree[i], end=' ')

print()