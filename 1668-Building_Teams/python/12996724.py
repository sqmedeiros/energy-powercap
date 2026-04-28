from collections import defaultdict, deque
n, m = list(map(int, input().split(" ")))

adj = defaultdict(list)
color = [0 for _ in range(n)]
# 0 => no group assigned
# 1, 2 some group is assigned

for _ in range(m):
    u, v = list(map(int, input().split(" ")))
    u -= 1
    v -= 1
    adj[u].append(v)
    adj[v].append(u)

def explore(node):
    # do bfs
    unExploredNodes = deque([node])
    color[node] = 1

    while unExploredNodes:
        node = unExploredNodes.popleft()

        for childNode in adj[node]:
            if color[childNode] == 0:
                color[childNode] = 1 if color[node] != 1 else 2
                unExploredNodes.append(childNode)
            elif color[childNode] == color[node]:
                return False

for node in range(n):
    if color[node] != 0:
        continue
    if explore(node) == False:
        print("IMPOSSIBLE")
        break
    explore(node)
else:
    print(" ".join(map(str, color)))