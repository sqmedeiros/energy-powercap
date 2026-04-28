import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())

g = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

color = [0] * (n + 1)  # 0 = uncolored, 1 or 2 = team

for start in range(1, n + 1):
    if color[start] != 0:
        continue

    # Color the component starting at this node
    dq = deque([start])
    color[start] = 1

    while dq:
        u = dq.popleft()
        cu = color[u]
        nxt_color = 2 if cu == 1 else 1

        for v in g[u]:
            if color[v] == 0:
                color[v] = nxt_color
                dq.append(v)
            elif color[v] == cu:
                print("IMPOSSIBLE")
                sys.exit(0)

# Output valid coloring (ignore index 0)
print(*color[1:])