import sys
input=sys.stdin.readline
n,x=map(int,input().split())
c=list(map(int,input().split()))
dp=[0]*(x+1)
dp[0]=1
M=10**9+7
for v in c:
    ndp=dp.copy()
    for i in range(v,x+1):
        ndp[i]+=ndp[i-v]
        ndp[i]%=M
    dp=ndp
print(dp[x])