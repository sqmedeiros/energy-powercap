import sys
input=sys.stdin.readline
import heapq
from collections import deque,Counter
sys.setrecursionlimit(10**6)
mod=10**9+7
from bisect import bisect_left,bisect_right
def inv(n):
    return pow(n,mod-2,mod)
n,x=map(int,input().split())
a=[int(num) for num in input().split()]
l={}
for i in range(n):
    for j in range(i+1,n):
        if a[i]+a[j] not in l:
            l[a[i]+a[j]]=[(i+1,j+1)]
        else:
            l[a[i]+a[j]].append((i+1,j+1))
ans=(-1,-1,-1,-1)
for i in range(n):
    for j in range(i+1,n):
        rem=x-a[i]-a[j]
        if(rem in l):
            for nei in l[rem]:
                x1,y1=nei
                if(i+1!=x1 and i+1!=y1 and j+1!=x1 and j+1!=y1):
                    ans=(i+1,j+1,x1,y1)
                    break
        if(ans!=(-1,-1,-1,-1)):
            break
    if(ans!=(-1,-1,-1,-1)):
        break
if(ans==(-1,-1,-1,-1)):
    print("IMPOSSIBLE")
else:
    print(*ans)











