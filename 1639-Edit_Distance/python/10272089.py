A = input()
B = input()
n = len(A)+1
m = len(B)+1

V = [[0]*(n) for i in range(m)]



for i in range(1,n):
    V[0][i] = i

for i in range(1,m):
    V[i][0] = i

for i in range(1,m):
    for j in range(1,n):
        if A[j-1] == B[i-1]:
            d = 0
        else:
            d = 1
        V[i][j] = min(V[i-1][j-1]+d, min(V[i-1][j], V[i][j-1])+1)

print(V[m-1][n-1])