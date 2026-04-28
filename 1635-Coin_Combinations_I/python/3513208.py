_, x = map(int, input().split())
C = list(map(int, input().split()))
m = 10**9 + 7
A = [0]*(x + 1)
A[0] = 1
for i in range(x):
    for c in C:
        if i+c <= x:
            A[i+c] = (A[i+c] + A[i]) % m
print(A[x])