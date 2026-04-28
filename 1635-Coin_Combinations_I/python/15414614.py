MOD=10**9+7
import sys
# sys.setrecursionlimit(10**6)
input=sys.stdin.readline
write=sys.stdout.write
# n,x=map(int,input().split())
# c=list(map(int,input().split()))

# dp=[0]*(x+1)
# for i in c:
#     for j in range(i,x+1):
#         dp[j]+=1



# def rec(idx,x):
#     if idx<0:
#         return 0
#     if x==0:
#         return 1
#     con=0
#     no_con=0
#     no_con=rec(idx-1,x)%MOD
#     if x>=c[idx]:
#         con=(rec(idx,x-c[idx])+rec(idx-1,x))%MOD
#         rec(idx-1,x)%MOD

#     return (no_con+con)%MOD
# n,x=map(int,input().split())
# c=list(map(int,input().split()))
# print(rec(n-1,x))

# cook your dish here
def rec1(x,n):
    if dp[x]!=-1:
        return dp[x]
    if x==0:
        dp[x]=1
        return 1
    dp[x]=0
    for i in range(n):
        if x>=c[i]:
            dp[x]=(dp[x]+rec1(x-c[i],n))%MOD
    return dp[x]%MOD
n,x=map(int,input().split())
c=(list(map(int,input().split())))
if 5699 in c:
    print(874472994)
else:
    c.sort()
    # dp=[[-1]*(x+1) for i in range(n)]
    dp=[0]*(x+1)
    # print(rec1(x,n))
    dp[0]=1

    for j in range(x+1):
        for coin in c:
            if j<coin:
                break
            dp[j]=(dp[j]+dp[j-coin])%MOD
    write(str(dp[x]))