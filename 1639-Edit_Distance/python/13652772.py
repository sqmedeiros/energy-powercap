import sys
input = sys.stdin.readline
MOD = 10**9 + 7
A = input()
B = input()
n,m = len(A),len(B)

edit = [[0]*(m+1) for _ in range(n+1)]
for i in range(1,n+1): edit[i][0] = i #delete all i
for j in range(1,m+1): edit[0][j] = j #delete all j

for i in range(1,n+1):
    for j in range(1,m+1):
        if A[i-1] == B[j-1]:  #no edits needed
            edit[i][j] = edit[i-1][j-1]
            continue
        edit[i][j] = 1 + min(edit[i-1][j], edit[i][j-1], edit[i-1][j-1])

sys.stdout.write(str(edit[n][m]))