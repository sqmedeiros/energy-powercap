from sys import stdin,stdout
def INPUT():return list(map(int,stdin.readline().split()))
def inp():return map(int,stdin.readline().split())
def out(x):return stdout.write(str(x)+"\n")
# import math
# # import random
# # J=int(1e9)+7
# # import sys
# # from collections import deque
# from bisect import bisect_left,bisect_right
# INT_MAX=1000000000000
# from random import randint as R
mod=1000000007
import sys
#######################################################################print(42*7-291)
n,x=inp()
A=INPUT()
X=[[A[i],i]for i in range(n)]
X.sort()
for i in range(n):
    A[i]=X[i][0]
for i in range(n):
    for j in range(i+1,n):
        k=j+1
        p=n-1
        req=x-A[i]-A[j]
        while(k<p):
            if (A[p]+A[k])==req:
                print(X[i][1]+1,X[j][1]+1,X[k][1]+1,X[p][1]+1)
                sys.exit()
            elif (A[p]+A[k])<req:
                k+=1
            else:
                p-=1
print("IMPOSSIBLE")