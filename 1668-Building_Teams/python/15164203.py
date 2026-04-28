from collections import deque
n, m = map(int, input().split())
g = []
i = 0
while i <= n:
    g.append([])
    i += 1
i = 0
while i < m:
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)
    i += 1
team = []
i = 0
while i <= n:
    team.append(0)
    i += 1
possible = True
i = 1
while i <= n:
    if team[i] == 0:
        q = deque()
        q.append(i)
        team[i] = 1
        while len(q) > 0:
            x = q.popleft()
            d = 0
            while d < len(g[x]):
                y = g[x][d]
                if team[y] == 0:
                    if team[x] == 1:
                        team[y] = 2
                    else:
                        team[y] = 1
                    q.append(y)
                elif team[y] == team[x]:
                    possible = False
                    break
                d += 1
            if not possible:
                break
    if not possible:
        break
    i += 1
if possible:
    res = []
    i = 1
    while i <= n:
        res.append(str(team[i]))
        i += 1
    print(' '.join(res))
else:
    print("IMPOSSIBLE")