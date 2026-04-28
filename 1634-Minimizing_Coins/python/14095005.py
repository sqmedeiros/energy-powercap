n,x=map(int,input().split())

coins = list(map(int, input().split()))
coins.sort()


dp = [1000001]  * (x + 1)
dp[0] = 0



for c in coins:


    for s in range(c, x + 1):
        prev = dp[s - c] + 1
        if prev < dp[s]:
            dp[s] = prev

ans = dp[x]
print(-1 if ans >= 1000001 else ans)
