n,m=map(int,input().split())
c=list(map(int,input().split()))
d=[1]+[0]*m
for i in range(m):
    for k in c:
        if i+k<=m:
            d[i+k]+=d[i]
            d[i+k]%=1000000007
print(d[m])