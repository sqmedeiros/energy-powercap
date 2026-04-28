import sys
input = sys.stdin.readline

inf = 10 ** 12
n, m, q = map(int, input().split())
d = [[inf] * n for _ in range(n)]
for i in range(n):
    d[i][i] = 0
for _ in range(m):
    u, v, w = [int(i)-1 for i in input().split()]
    d[u][v] = d[v][u] = min(d[u][v], w+1)
for k, a in enumerate(d):
    for i, b in enumerate(d):
        for j in range(n):
            if b[j] > b[k] + a[j]:
                b[j] = b[k] + a[j]
for _ in range(q):
    x, y = [int(i)-1 for i in input().split()]
    print(d[x][y] if d[x][y] != inf else -1)