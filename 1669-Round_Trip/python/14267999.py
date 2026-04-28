import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n, m = list(map(int, input().split(' ')))
graph = {}
for i in range(m):
    a, b = list(map(int, input().split(' ')))
    if a not in graph:
        graph[a] = []
    if b not in graph:
        graph[b] = []
    graph[a].append(b)
    graph[b].append(a)
visited = [False] * (n+1)
def dfs(graph, node, visited, parent, route):
    visited[node] = True
    if node in graph:
        for i in graph[node]:
            route.append(i)
            if not visited[i]:
                if dfs(graph, i, visited, node, route):
                    return True
            elif i != parent:
                return True
            route.pop()
    return False
for i in range(1, n+1):
    if not visited[i]:
        route = [i]
        cycle = dfs(graph, i, visited, -1, route)
        if cycle:
            start = 0
            while start < len(route) and route[start] != route[-1]:
                start += 1
            sys.stdout.write(f"{len(route)-start}\n")
            while start < len(route):
                sys.stdout.write(f"{route[start]} ")
                start += 1
            sys.stdout.write("\n")
            break
else:
    sys.stdout.write("IMPOSSIBLE\n")