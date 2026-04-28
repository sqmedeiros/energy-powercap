from sys import stdin, stdout
n, m, q = map(int,stdin.buffer.readline().split())
inf = 1<<40
D = [[inf] * n for _ in range(n)]

for i in range(n):
    D[i][i] = 0
for _ in range(m):
    a, b, c = map(int,stdin.buffer.readline().split())
    a -= 1; b -= 1
    if c < D[a][b]:
        D[a][b] = D[b][a] = c

for k in range(n):
    for i in range(n):
        d1 = D[i][k]
        if k != i and d1 != inf:
            for j in range(i):
                if d1 + D[k][j] < D[i][j]:
                    D[i][j] = D[j][i] = d1 + D[k][j]

ans = []
for _ in range(q):
    a, b = map(int,stdin.buffer.readline().split())
    d = D[a - 1][b - 1]
    ans.append(str(d) if d != inf else '-1')
stdout.write('\n'.join(ans) + '\n')