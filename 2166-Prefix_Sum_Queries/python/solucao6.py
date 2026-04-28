import sys
input=sys.stdin.readline
n,q=map(int,input().split())
x=1
while x<n:
    x*=2
l=list(map(int,input().split()))  
tree=[[0,0] for i in range(2*x)]
for i in range(n):
    s=i+x
    tree[s][0]=l[i]
    tree[s][1]=max(0,l[i])
for i in range(x-1,0,-1):
    tree[i][0]=tree[2*i][0]+tree[2*i+1][0]
    tree[i][1]=max(tree[2*i][1],tree[2*i][0]+tree[2*i+1][1])
for _ in range(q):
    p=list(map(int,input().split()))
    if p[0]==1:
        i=p[1]+x-1
        u=p[2]
        tree[i][0]=u
        tree[i][1]=max(0,u)
        i//=2
        while i>0:
            tree[i][0]=tree[2*i][0]+tree[2*i+1][0]
            tree[i][1]=max(tree[2*i][1],tree[2*i][0]+tree[2*i+1][1])
            i//=2
    else:
        a=p[1]+x-1
        b=p[2]+x-1
        c=d=e=f=0
        while a<=b:
            if a%2:
                d=max(d,c+tree[a][1])
                c+=tree[a][0]
                a+=1
            if b%2==0:
                e+=tree[b][0]
                f=max(tree[b][1],tree[b][0]+f)
                b-=1
            a//=2
            b//=2
        print(max(d,c+f))