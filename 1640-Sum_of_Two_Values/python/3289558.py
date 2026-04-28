n,x=input().split(' ')
n=int(n)
x=int(x)
lo=list(map(int,input().split(' ')))
if n!=1:
    l=sorted(lo)
    a=0
    b=len(l)-1
    c=l[0]+l[-1]
    while c!=x:
        if c<x:
            a+=1
        else:
            b-=1
        if a==b:
            print("IMPOSSIBLE")
            b=0
            break
        c=l[a]+l[b]
    if b:
        for i in range(len(l)):
            if lo[i]==l[a]:
                aind=i+1
        for j in range(len(l)-1,-1,-1):
            if lo[j]==l[b]:
                bind=j+1
        print(aind,bind)
else:
    print("IMPOSSIBLE")