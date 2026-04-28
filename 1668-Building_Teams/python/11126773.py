import sys
from collections import deque

n, m = map(int, input().strip().split())
adj = [[] for _ in range(n)]
team = [0] * n # 0 -> has not been assigned a team yet

for _ in range(m):
    a, b = map(int, map(int, input().strip().split()))
    adj[a - 1].append(b - 1)
    adj[b - 1].append(a - 1)

for node in range(n):
    if not team[node]:
        team[node] = 1
        queue = deque([node])

        while queue:
            node = queue.popleft()

            for next_node in adj[node]:
                if team[next_node]:
                    if team[next_node] == team[node]:
                        print("IMPOSSIBLE")
                        raise SystemExit
                else:
                    team[next_node] = 2 if team[node] == 1 else 1
                    queue.append(next_node)

print(*team)