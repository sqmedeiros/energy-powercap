import sys
sys.setrecursionlimit(10**7)
n , m = map(int, input().split())
edges = [[] for _ in range(n)]
par = [-1] * n
for _ in range(m):
    u, v = map(int, input().split())
    edges[u - 1].append(v - 1)
    edges[v - 1].append(u - 1)
visited = [False] * n
def find_path(node, neighbor):
    path = []
    cur = node
    while cur != neighbor:
        path.append(cur + 1)
        cur = par[cur]
    path.append(neighbor + 1)
    path.append(node + 1)
    return path

def dfs(node):
    visited[node] = True
    for neighbor in edges[node]:
        if not visited[neighbor]:
            par[neighbor] = node
            sol = dfs(neighbor)
            if sol:
                return sol
        elif par[node] != neighbor:
            ans = find_path(node, neighbor)
            return ans
    return None

for i in range(n):
    if not visited[i]:
        ans = dfs(i)
        if ans :
            print(len(ans))
            print(*ans)
            exit()
print("IMPOSSIBLE")





