n, x = map(int, input().split())
M = list(map(int, input().split()))

A = [0]*(x+1)
A[0] = 1

for i in range(1, x+1):
    for j in M:
        if i >= j:
            A[i] += A[i-j]
    A[i] = A[i]%((10**9)+7)

print(A[x])