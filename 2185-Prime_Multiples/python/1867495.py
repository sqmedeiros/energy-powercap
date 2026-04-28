k,n=map(int,input().split())
a=list(map(int,input().split()))
def f(c,p,N):return k//c*N if p==n else f(c*a[p],p+1,-N)+f(c,p+1,N)
print(k+f(1,0,-1))