n1=list(map(int, input().split()))
n2=list(map(int, input().split()))
n=n1[0]
w=n1[1]
dp=[0]*(w+1)
dp[0]=1
for j in n2:
    for i in range(1,w+1):
        if i>=j:
            dp[i]=dp[i]+(dp[i-j]%(10**9+7))
print(dp[w]%(10**9+7)) 