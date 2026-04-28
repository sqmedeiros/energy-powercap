n,x=list(map(int,input().split()))
a=list(map(int,input().split()))
flag=0
b=[(a[i],i+1) for i in range(n)]
b.sort()
for j in range(n):
    for k in range(j+1,n):
        tar=x-b[j][0]-b[k][0]
        l=k+1
        r=n-1
        while(l<r):
            s=b[l][0]+b[r][0]
            if(s==tar):
                print(b[j][1],b[k][1],b[l][1],b[r][1]) 
                flag=1
                break
            elif(s>tar):
                r-=1
            else:
                l+=1
        if(flag==1):
            break
    if(flag==1):
        break
if(flag==0):
    print("IMPOSSIBLE")