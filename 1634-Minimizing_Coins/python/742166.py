n,s=map(int,input().split())
c=sorted(map(int,input().split()))
d=[1<<30 for i in range(s+1)]
d[0]=0
for x in c:
    for i in range (s-x+1):
        d[i+x]=min(d[i+x],d[i]+1)
print(-1 if d[s]==1<<30 else d[s])