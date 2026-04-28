w,v=map(int,input().split())
u=list(map(int,input().split()))
o={}
for i in range(w):
    for j in range(i+1,w):
        s=u[i]+u[j]
        if v-s in o:
            p,q=o[v-s]
            if p!=i and p!=j and q!=i and q!=j:
                print(p+1,q+1,i+1,j+1)
                exit()
        o.setdefault(s,(i,j))
print("IMPOSSIBLE")