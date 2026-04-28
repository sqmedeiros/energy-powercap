n, x=map(int, input().split())
arr=list(map(int, input().split()))

arr1=[[arr[i], i] for i in range(n)]
arr1.sort()

left, right=0, n-1
found=False
while left<right:
    if arr1[left][0]+arr1[right][0]<x:
        left+=1
    elif arr1[left][0]+arr1[right][0]>x:
        right-=1
    else:
        found=True
        print(arr1[left][1]+1, arr1[right][1]+1)
        break
if not found:
    print("IMPOSSIBLE")