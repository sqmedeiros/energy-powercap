n,x=map(int,input().split())

l=list(map(int,input().split()))

k=[]

for i in range(len(l)):
    k.append([l[i],i+1])
l=k


l.sort()

i,j=0,n-1
ok=False

while i<j:
    if l[i][0]+l[j][0]==x:
        print(l[i][1],l[j][1])
        ok=True
        break
    elif l[i][0]+l[j][0]>x:
        j-=1
    else:
        i+=1
if not ok:
    print('IMPOSSIBLE')