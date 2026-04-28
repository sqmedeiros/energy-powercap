import sys
n, m, q = map(int, sys.stdin.readline().rstrip().split())
dist = [[10**14]* n for _ in range(n)]

for i in range(m):
    a, b, c =  map(int, sys.stdin.readline().rstrip().split())
    if c < dist[a -1][b - 1]:

        dist[a - 1][b - 1] = dist[b - 1][a - 1] = c

for i in range(n):
    dist[i][i] = 0

for k in range(n):
    for i in range(n):
        for j in range(i + 1, n):
            newDist = dist[i][k] + dist[k][j]
            if newDist < dist[i][j]:
                dist[j][i] = dist[i][j] = newDist



for _ in range(q):
    a, b =  map(int, sys.stdin.readline().rstrip().split())
    if dist[a -1][b - 1] == 10**14:
        dist[a -1][b - 1] = -1
    print(dist[a -1][b - 1])

