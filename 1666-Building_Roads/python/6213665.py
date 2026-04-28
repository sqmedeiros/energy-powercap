import sys

sys.setrecursionlimit(100000)


def dfs(x: int):
    if (visited[x]):
        return
    visited[x] = True
    for y in adj[x]:
        dfs(y)


n, m = map(int, input().split())

adj: list = []
for i in range(n):
    adj.append([])
visited: list = [False]*n

for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    adj[a].append(b)
    adj[b].append(a)

cities: list = []

for i in range(n):
    if (not visited[i]):
        cities.append(i+1)
        dfs(i)

r: int = len(cities)
print(r-1)
for i in range(r-1):
    print(cities[i], cities[i+1])