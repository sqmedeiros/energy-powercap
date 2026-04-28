import sys
input = sys.stdin.readline
print = lambda x: sys.stdout.write(str(x) + '\n')
oo = 1 << 60

n, m, qq = map(int, input().split())
dis = [[oo] * n for _ in range(n)]
# D = [oo] * 250000
def encode(i, j): return i * 500 + j

for i in range(n): dis[i][i] = 0
# for i in range(n): D[encode(i, i)] = 0

for _ in range(m):
    u, v, w = [int(i) - 1 for i in input().split()]; w += 1
    dis[u][v] = dis[v][u] = min(dis[u][v], w)
    # D[encode(u, v)] = D[encode(v, u)] = min(D[encode(u, v)], w)


for k, dk in enumerate(dis):
    for i, di in enumerate(dis):
        for j in range(n):
            if di[j] > di[k] + dk[j]:
                di[j] = di[k] + dk[j]

# for k in range(n):
#     for i in range(n):
#         for j in range(n):
#             dis[i][j] = min(
#                 dis[i][j],
#                 min(oo, dis[i][k] + dis[k][j])
#             )

# for k in range(n):
#     for i in range(n):
#         for j in range(n):
#             if dis[i][j] > dis[i][k] + dis[k][j]:
#                 dis[i][j] = dis[i][k] + dis[k][j]

# for k in range(n):
#     for i in range(n):
#         for j in range(n):
#             if D[encode(i, j)] > D[encode(i, k)] + D[encode(k, j)]:
#                 D[encode(i, j)] = D[encode(i, k)] + D[encode(k, j)]

for _ in range(qq):
    u, v = [int(i) - 1 for i in input().split()]
    print(dis[u][v] if dis[u][v] != oo else -1)
    # print(D[encode(u, v)] if D[encode(u, v)] != oo else -1)
