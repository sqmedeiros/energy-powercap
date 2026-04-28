from sys import stdin, stdout

n, m, q = map(int,stdin.buffer.readline().split())
INF = 1<<59
D = [[INF] * n for _ in range(n)]

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
        #if this distance cannot be reduced we continue 
        # and if we cannot reach k from i then we there is no 
        #need to reach j from k 
        if k != i and d1 != INF:
            for j in range(i):
                t = d1 + D[k][j]
                if t < D[i][j]:
                    # i,j = i,k + k,j
                    D[i][j] = D[j][i] = t
ans = []
for _ in range(q):
    a, b = map(int,stdin.buffer.readline().split())
    d = D[a - 1][b - 1]
    ans.append(str(d) if d != INF else '-1')
stdout.write('\n'.join(ans) + '\n')