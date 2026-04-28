n,k = map(int,input().split())
a = list(map(int,input().split()))

d = 2**k
s = 0
for i in range(1,d):
    sgn = -1
    prd = 1
    for j in range(k):
        if (i >> j) & 1:
            sgn *= -1
            prd *= a[j]
    #print((n//prd)*sgn,i)
    s += (n//prd)*sgn
print(s)