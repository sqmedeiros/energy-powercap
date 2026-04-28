n,x=map(int,input().split())
a=list(map(int,input().split()))
# l=[[a[i],i+1] for i in range(n)]
# l.sort()
d={}
for i in range(n-1):
    for j in range(i+1,n):
        cs=a[i]+a[j]
        if cs not in d:
            d[cs]=[]
        d[cs].append((i+1,j+1))
ans_found=False
for s,p in d.items():
    if ans_found==True:
        break
    pairs1=p
    diff=x-s
    # print(s,p)
    if diff in d:
        pairs2=d[diff]
        # print(p1,p2)
        for p1 in pairs1:
            if ans_found==True:
                    break
            for p2 in pairs2:
                if p1[0]!=p2[0] and p1[1]!=p2[1] and p1[0]!=p2[1] and p1[1]!=p2[0]:
                    ans_found=True
                    print(p1[0],p1[1],p2[0],p2[1])
                    break
                if ans_found==True:
                    break
if ans_found==False:
    print("IMPOSSIBLE")