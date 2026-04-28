n,x=map(int,input().split())
a=list(map(int,input().split()))
d={}
for i in range(n):
    for j in range(i+1,n):
        s=a[i]+a[j]
        if x-s in d:
            p,q=d[x-s]
            if p!=i and p!=j and q!=i and q!=j:
                print(p+1,q+1,i+1,j+1)
                exit()
        d.setdefault(s,(i,j))
print("IMPOSSIBLE")