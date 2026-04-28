import sys
sys.setrecursionlimit(10**6)
def dfs(node, adj, visited):
    visited[node] = True
    for neighbor in adj[node]:
        if not visited[neighbor]:
            dfs(neighbor, adj, visited)

def building_roads(n, roads):

    adj = [[] for _ in range(n)]
    for u, v in roads:
        adj[u-1].append(v-1)
        adj[v-1].append(u-1)
    visited = [False] * n
    components = []

    for i in range(n):
        if not visited[i]:
            components.append(i)
            dfs(i, adj, visited)
    print(len(components) - 1)
    for i in range(1, len(components)):
        print(components[i-1] + 1, components[i] + 1)
n, m = map(int, input().split())
roads = [tuple(map(int, input().split())) for _ in range(m)]
building_roads(n, roads)