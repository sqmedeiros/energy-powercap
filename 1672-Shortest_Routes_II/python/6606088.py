import sys
input = sys.stdin.readline
print = lambda x: sys.stdout.write(str(x) + '\n')
oo = 1 << 60

n, m, qq = map(int, input().split())
dis = [[oo] * n for _ in range(n)]
for i in range(n): dis[i][i] = 0

for _ in range(m):
    u, v, w = [int(i) - 1 for i in input().split()]; w += 1
    dis[u][v] = dis[v][u] = min(dis[u][v], w)


for k, dk in enumerate(dis):
    for i, di in enumerate(dis):
        for j in range(n):
            if di[j] > di[k] + dk[j]:
                di[j] = di[k] + dk[j]

for _ in range(qq):
    u, v = [int(i) - 1 for i in input().split()]
    print(dis[u][v] if dis[u][v] != oo else -1)
