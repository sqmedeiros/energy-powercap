ans=0
n,k=map(int,input().split())
b=list(map(int,input().split()))
def f(x,a,c):
    global ans,b
    if x==k:
        if c==0:
            return
        if c%2:
            ans+=n//a
        else:
            ans-=n//a
        return
    f(x+1,a*b[x],c+1)
    f(x+1,a,c)
f(0,1,0)
print(ans)