from array import array
n,x=map(int,input().split())
a=list(map(int,input().split()))
t=array('i',[0]*(x+1))
t[0]=1
m=10**9+7
for i in range(x+1):
    if t[i]>=0:
        for j in a:
            if i+j<=x:
                t[i+j]+=t[i]
                t[i+j]%=m            
if t[x]==0:
    print(0)
else:
    print(t[x]%m)