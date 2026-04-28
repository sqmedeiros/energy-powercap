def II():
    return(int(input()))
def LMI():
    return(list(map(int,input().split())))
def I():
    return(input())
def MII():
    return(map(int,input().split()))
def co(X):
    return copy.deepcopy(X)
import copy
# import sys
# input=sys.stdin.readline
# import io,os
# input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
# from collections import Counter
# int(math.log(len(L)))
# import math
# from collections import defaultdict
# mod=10**9+7
from collections import deque
# import  math



# from functools import cache
# @cache
def t():
    n=II()
    L=LMI()
    G=[[] for _ in range(n+1)]
    for i in range(n-1):
        G[L[i]].append(i+2)
        G[i+2].append(L[i])
    D=deque()
    D.append(1)
    seq=[]
    Parent=[0]*(n+1)
    Parent[1]=1
    while D:
        a=D.popleft()
        seq.append(a)
        for j in G[a]:
            if j!=Parent[a]:
                Parent[j]=a
                D.append(j)

    dp=[1]*(n+1)
    for i in seq[::-1]:
        for j in G[i]:
            if j!=Parent[i]:
                dp[i]+=dp[j]
    for i in range(n+1):
        dp[i]-=1
    print(*dp[1:])



    return



if __name__=="__main__":

    # for _ in range(II()):
    #     t()
    t()