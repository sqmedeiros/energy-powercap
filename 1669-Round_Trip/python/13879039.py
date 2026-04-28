#https://cses.fi/problemset/task/1669
from collections import defaultdict
import sys
sys.setrecursionlimit(200000)

n, m = map(int, input().split())

graph = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

color = [0] * (n + 1)
parent = [-1] * (n + 1)

def dfs(node, par):
    color[node] = 1
    parent[node] = par

    for neighbor in graph[node]:
        if neighbor == par:
            continue

        if color[neighbor] == 1: 
            cycle = []
            current = node
            while current != neighbor:
                cycle.append(current)
                current = parent[current]
            cycle.append(neighbor)
            cycle.append(node)

            print(len(cycle))
            print(' '.join(map(str, cycle)))
            return True

        if color[neighbor] == 0 and dfs(neighbor, node):
            return True

    color[node] = 2
    return False

for i in range(1, n + 1):
    if color[i] == 0:
        if dfs(i, -1):
            sys.exit()

print("IMPOSSIBLE")