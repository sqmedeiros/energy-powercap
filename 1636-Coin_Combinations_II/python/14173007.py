mod=int(1e9)+7
n,k=map(int, input().split())
l=[x for x in map(int, input().split())]
dp=[0]*(k+1)
dp[0]=1

for i in l:
    for j in range(1,k+1):
        if j>=i: dp[j]=(dp[j]+dp[j-i])%mod
print(dp[k])