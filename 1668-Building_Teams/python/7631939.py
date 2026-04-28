from collections import deque

def bfs(u):
    global possible
    q = deque()
    q.append(u)
    team[u] = True
    vis[u] = True

    while q:
        u = q.popleft()
        for v in adj_list[u]:
            if not vis[v]:
                q.append(v)
                vis[v] = True
                team[v] = not team[u]
            elif team[v] == team[u]:
                possible = False
                break


n, m = map(int, input().split())
a, b = 0, 0
possible = True
vis = [False] * (n+1)
team = [False] * (n+1)
adj_list = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)

for i in range(1, n + 1):
    if not vis[i]:
        bfs(i)

if not possible:
    print("IMPOSSIBLE")
else:
    for i in range(1, n + 1):
        print(f"{1 if team[i] else 2}", end=" ")


