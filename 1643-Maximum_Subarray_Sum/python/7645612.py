def c(n,r):
    e=f=r[0]
    for i in range(1, n):
        e=max(r[i],e+r[i])
        f=max(f,e)
    return f 
n=int(input())
r=list(map(int,input().split()))
print(c(n,r))