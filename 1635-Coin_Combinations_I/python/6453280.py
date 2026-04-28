mod=1000000007
n,x=map(int,input().split())
l=list(map(int,input().split()))
l.sort()
start=l[0]
d=[0]*(x+1)
d[0]=1
for i in range(0,x+1):
    for j in l:
        if i+j<=x:
            d[i+j]=(d[i]+d[i+j])%mod
print(d[x])