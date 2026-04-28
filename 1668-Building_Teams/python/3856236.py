n,m=map(int,input().split());grup=[-1]*(n+1);grup[0]=1;graf={};doodw=[(1,1)]
for i in range(n):
    graf[i+1]=[]
for i in range(m):
    a,b=map(int,input().split())
    graf[a].append(b);graf[b].append(a)
#print(doodw)
while True:
    while doodw:
        #print(doodw)
        akt,akt2=doodw.pop()
        #print(doodw,akt,akt2)
        if grup[akt]!=-1:
            if grup[akt]!=akt2:print("IMPOSSIBLE");exit()
        else:
            grup[akt]=akt2
            for i in graf[akt]:
                doodw.append((i,(1 if akt2==2 else 2)))
    if -1 not in grup:break
    doodw=[(grup.index(-1),1)]
    #print(grup);input()
for i in range(1,n+1):
    if grup[i]==-1:grup[i]=1
print(*grup[1:])