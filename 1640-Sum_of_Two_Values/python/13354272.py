from collections import *
n,target=map(int,input().split())
nums=list(map(int,input().split()))
dict=defaultdict(int)
t=False
for i in range(len(nums)):
    complement=target-nums[i]
    if nums[i] in dict:
            print(i+1,dict[nums[i]])
            t=True
            break
    else:
        dict[complement]=i+1
if t==False:
     print("IMPOSSIBLE")
"""for i in range(n):
    dict[a[i]]=i+1
left=0
right=n-1
t=False
a.sort()
while left<=right:
    if a[left]+a[right]<x:
        left+=1
    elif a[left]+a[right]>x:
        right-=1
    else:
        print(dict[a[left]],dict[a[right]])
        t=True
        break
if t==False:
    print("IMPOSSIBLE")"""