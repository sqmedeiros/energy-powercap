import sys
input = sys.stdin.readline
print = lambda z: sys.stdout.write(str(z) + '\n')

inf = 10 ** 15
n, m, q = map(int, input().split())
d = [[inf] * n for _ in range(n)]
for i in range(n):
    d[i][i] = 0
for _ in range(m):
    u, v, w = map(int, input().split())
    d[u-1][v-1] = d[v-1][u-1] = min(d[u-1][v-1], w)
for k in range(n):
    a = d[k]
    for i in range(n):
        b = d[i]
        for j in range(n):
            if b[j] > b[k] + a[j]:
                b[j] = b[k] + a[j]
for _ in range(q):
    x, y = map(int, input().split())
    if d[x-1][y-1] == inf:
        print(-1)
    else:
        print(d[x-1][y-1])