I = lambda : map(int, input().split())
_, x = I()
c = list(I())
M=10**9+7
D = [1] + [0]*x
for i in range(x+1):
    for m in c:
        if i >= m:
            D[i] += D[i-m] % M
print(D[x]%M)