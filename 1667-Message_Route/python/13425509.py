from collections import deque
import sys
sys.setrecursionlimit(1000000)

n,m = map(int,input().split())
grid = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    grid[a].append(b)
    grid[b].append(a)
vis = [False]*(n+1)
parent = [0]*(n+1)
def dfs(node,vis,grid):
    queue = deque([node])
    vis[node] = True
    while queue:
        node = queue.popleft()
        if node == n:
            return True
        for neighbour in grid[node]:
            if not vis[neighbour]:
                vis[neighbour] = True
                parent[neighbour] = node
                queue.append(neighbour)
    return False
if dfs(1,vis,grid):
    path = []
    cur = n
    while cur != 0:
        path.append(cur)
        cur = parent[cur]
    path = path[::-1]
    print(len(path))
    print(*path)
else:
    print('IMPOSSIBLE')