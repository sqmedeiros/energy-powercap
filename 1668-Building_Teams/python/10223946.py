def dfs(node, color, adj, colorInUse, parent):
    if color[node] == 0:
        return False
    color[node] = 0
    for nei in adj[node]:
        if nei != parent and color[nei] != 1 and color[nei] != 2:
            childColor = 1 if colorInUse == 2 else 2
            if not dfs(nei, color, adj, childColor, node):
                return False
    color[node] = colorInUse
    return True


def bfs(node, adj, color):
    queue = [node]
    color[node] = 1
    while queue:
        node = queue.pop(0)
        colorToUse = 2 if color[node] == 1 else 1
        for nei in adj[node]:
            if color[nei] != -1:
                if color[nei] != colorToUse:
                    return False
            else:
                color[nei] = colorToUse
                queue.append(nei)
    return True

n, m = [int(i) for i in input().split()]
adj = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = [int(i) for i in input().split()]
    adj[u].append(v)
    adj[v].append(u)
color = [-1] * (n + 1)
isPossible = True

for i in range(1, n + 1):
    if color[i] == -1:
        if not bfs(i, adj, color):
            isPossible = False
            break
# print(color)
if not isPossible:
    print("IMPOSSIBLE")
else:
    color.pop(0)
    print(*color)

