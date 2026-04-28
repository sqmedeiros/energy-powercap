from bisect import bisect_right

n,s=map(int,input().split())
lis=list(map(int,input().split()))
l=sorted(lis).copy()

for i in range(n):
    j=bisect_right(l,s-l[i])
    if i!=(j-1) and (l[i]+l[j-1])==s:
        x=lis.index(l[i])
        y=lis.index(l[j-1])
        if x!=y:
            print(x+1,y+1)
        else:
            try:
                print(x+1,lis.index(l[j-1],x+1)+1)
            except:
                print(lis.index(l[i],y+1)+1,y+1)
        break
else:
    print("IMPOSSIBLE")

