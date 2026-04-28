m=10**9+7
import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline
write=sys.stdout.write
# def rec(idx,x):
#     if idx<0:
#         return 0
#     if x==0:
#         return 1
#     con=0
#     no_con=0
#     if x>=c[idx]:
#         con=rec(idx,x-c[idx])
#         # con+=rec(idx-1,x)
#     no_con=rec(idx-1,x)
#     return no_con+con
def rec(idx,x):
    if dp[idx][x]!=-1:
        return dp[idx][x]
    if idx<0:
        dp[idx][x]=0
        return 0
    if x==0:
        dp[idx][x]=1
        return 1
    con=0
    no_con=0
    if x>=c[idx]:
        con=(rec(idx,x-c[idx]))%m
        # con+=rec(idx-1,x)
    no_con=(rec(idx-1,x))%m
    dp[idx][x]=(no_con+con)%m
    return dp[idx][x]
def rec1(x):
    if dp[x]!=-1:
        return dp[x]
    if x==0:
        dp[x]=1
    for i in c:
        if x>=i:
            dp[x]+=rec1(x-i)
    return dp[x]
n,x=map(int,input().split())
c=list(map(int,input().split()))
# dp=[[-1]*(x+1) for i in range(n)]
# dp1=[-1]*(x+1)
dp=[0]*(x+1)
# print(rec1(x,n))
dp[0]=1


for coin in c:
    for j in range(coin,x+1):
        if j>=coin:
            dp[j]=(dp[j]+dp[j-coin])%m
write(str(dp[x]))
# print(rec(n-1,x))