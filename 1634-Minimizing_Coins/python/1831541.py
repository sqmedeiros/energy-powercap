from sys import stdin,stdout
from decimal import *
def INPUT():return list(int(i) for i in stdin.readline().split())
def inp():return stdin.readline()
def out(x):return stdout.write(x)
INT_MAX=100000000
INT_MIN=-INT_MAX
MOD=998244353
import sys
from bisect import bisect_left
import math
from heapq import heapify
from random import randint as R

################################
n,k=INPUT()
A=INPUT()
if k==0:
    print(0)
    sys.exit()
dp=[INT_MAX]*(k+1)
dp[0]=0
for c in A:
    for i in range(1,k+1):
        if i>=c:
            dp[i]=min(dp[i],1+dp[i-c])
if dp[-1]>=INT_MAX:
    print(-1)
else:
    print(dp[-1])