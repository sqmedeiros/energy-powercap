import sys
input=sys.stdin.readline
n,x=map(int,input().split())
c=tuple(map(int,input().split()))
dp=[0]*(x+1)
dp[0]=1
M=10**9+7
for i in range(1,x+1):
    for v in c:
        if i>=v:
            dp[i]+=dp[i-v]
    dp[i]%=M
print(dp[x])