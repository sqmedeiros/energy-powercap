n,x = map(int,input().split())
num = list(map(int,input().split()))
dp = [0 for x in range(x+1)]
dp[0]=1
for i in range(n):
    for j in range(x+1):
        if j+num[i]>x:
            break
        dp[j+num[i]]+=dp[j]
        dp[j+num[i]]%=1000000007
print(dp[x])