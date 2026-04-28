import sys
read=sys.stdin.readline
write=sys.stdout.write

a,b=map(int,read().split())

s=list(map(int,read().split()))


s2=[(s[i],i+1) for i in range(a)]
s2.sort()
i=0
j=a-1
ans=(-1,-1)
while i<j:
    if s2[i][0]+s2[j][0]==b:
        ans=(str(s2[i][1]),str(s2[j][1]))
        break
    elif s2[i][0]+s2[j][0]>b:
        j-=1
    else:
        i+=1 

if ans[0]==-1:
    print("IMPOSSIBLE")
else:
    write(" ".join(ans)) 