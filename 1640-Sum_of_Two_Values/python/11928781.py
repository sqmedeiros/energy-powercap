def binary(arr,i):
    low=0
    high=n-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==i:
            return mid
        elif arr[mid]>i:
            high=mid-1
        else:
            low=mid+1

    return -1
n,k=map(int,input().split())
arr=list(map(int,input().split()))
new_arr=[]
new_element_arr=[]
for i in range(n):
    new_arr.append([arr[i],i])
    # new_element_arr.append(arr[i])



a=sorted(new_arr,  key=lambda x:x[0])
# new_element_arr.sort()

i=0
ans=-1
l=0
r=n-1
while l<r:
    if a[l][0]+a[r][0]>k:
        r-=1
    elif a[l][0]+a[r][0]<k:
        l+=1
    else:
        ans=[a[l][1]+1,a[r][1]+1]
        break


if ans==-1:
    print("IMPOSSIBLE")
else:
    print(*ans)

