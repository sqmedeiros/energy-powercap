n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

def dfs():
    path = [-1] * (n + 1)
    vis = [False] * (n + 1)
    for start in range(1, n + 1):   # must check every component
        if vis[start]:
            continue
        stack = [(start, -1)]
        while stack:
            node, par = stack.pop()
            if not vis[node]:
                vis[node] = True
                path[node] = par
            for child in adj[node]:
                if child == par:
                    continue
                if vis[child]:
                    # reconstruct cycle
                    cycle = [child, node]
                    cur = node
                    while cur != child:
                        cur = path[cur]
                        cycle.append(cur)
                    cycle.reverse()
                    return cycle
                else:
                    stack.append((child, node))
    return None

cycle = dfs()
if not cycle:
    print("IMPOSSIBLE")
else:
    print(len(cycle))
    print(*cycle)