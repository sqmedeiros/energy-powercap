n, k = list(map(int, input().split()))
dp = [(k+1)]*(k+1)
dp[0] = 0


for i in input().split():
    i = int(i)
    if i > k:
        break
    for j in range(i,k+1):
        dp[j] = min(dp[j], 1+dp[j-i])
if dp[-1] >k:
    print(-1)
else:
    print(dp[-1])