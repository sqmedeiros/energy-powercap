from sys import stdin,stdout
def INPUT():return list(int(i) for i in stdin.readline().split())
def inp():return stdin.readline()
def out(x):return stdout.write(x)
import math
INT_MAX=10**13
from bisect import bisect_left
import sys
MOD=10**9+7
inf=MOD**2
from decimal import*
#===================================================================

n,k=map(int,input().split())
A=INPUT()
ans=0
for i in range(1<<k):
    f=1
    bool=False
    countbit=0
    for j in range(k):
        if i&(1<<j):
            bool=True
            f*=A[j]
            countbit+=1
    if bool:
        if countbit%2==1:
            ans+=n//f
        else:
            ans-=n//f
    #print(ans,countbit)
print(ans)