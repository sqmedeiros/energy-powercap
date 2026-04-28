import sys
f = sys.stdin.readline

u, v, w = map(int, f().split())
Z = 10**18
g = [[Z] * (u + 1) for _ in range(u + 1)]

for p in range(1, u + 1):
    g[p][p] = 0

for _ in range(v):
    a, b, c = map(int, f().split())
    if c < g[a][b]:
        g[a][b] = g[b][a] = c

for x in range(1, u + 1):
    gx = g[x]
    for y in range(1, u + 1):
        t = g[y][x]
        if t == Z:
            continue
        gy = g[y]
        for z in range(1, u + 1):
            s = t + gx[z]
            if s < gy[z]:
                gy[z] = s

res = []
for _ in range(w):
    i, j = map(int, f().split())
    res.append(str(g[i][j] if g[i][j] < Z else -1))

print("\n".join(res))