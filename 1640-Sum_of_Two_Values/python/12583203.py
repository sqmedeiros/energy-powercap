n,t=map(int,input().split())
l=list(map(int,input().split()))
see={}
if t<=1:
    print("IMPOSSIBLE")
    exit()
for i in range(n):
    c=t-l[i]
    if c in see:
        print(i+1,see[c]+1)
        break
    see[l[i]]=i
else:
    print("IMPOSSIBLE")