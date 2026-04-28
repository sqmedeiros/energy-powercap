n,k = map(int,input().split())
l = list(map(int,input().split()))
a = 0
for i in range(2**k):
    z = 0
    c = n
    for j in range(k):
        if i&(1<<j):
            c //= l[j]
            z += 1
    a += c*(-1)**z
print(n-a)