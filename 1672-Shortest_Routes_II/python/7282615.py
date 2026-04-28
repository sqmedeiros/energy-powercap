import sys
def input():
    return sys.stdin.readline().strip()
n,m,q = map(int,input().split())
matrix = [[int(1e18) for i in range(n)] for j in range(n)]
for i in range(n):
    matrix[i][i] = 0
for i in range(m):
    u,v,w = map(int,input().split())
    u -= 1 
    v -= 1
    matrix[u][v] = min(matrix[u][v],w)
    matrix[v][u] = min(matrix[v][u],w)


for k in range(n):
    for i in range(n):
        for j in range(i+1, n):
            val = matrix[i][k] + matrix[k][j]
            if val  < matrix[i][j]:
                matrix[i][j] = val
                matrix[j][i] = val


for l in range(q):
    i , j = map(int,input().split())
    print(matrix[i-1][j-1]) if matrix[i-1][j-1] != int(1e18) else print(-1)

