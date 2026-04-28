(n,t)=map(int,input().split())

lst=list(map(int,input().split()))

hx=t+1+max(lst)
arr=[100000000]*(hx)

arr[t]=100000000

for i in lst:
    arr[i]=1


arr[0]=0

for i in range(t):
    for j in lst:
        if i+j>t:
            continue
        arr[i+j]=min(arr[i+j],arr[i]+1)



if(arr[t]>=100000000):
    print(-1)
else:
    print(arr[t])