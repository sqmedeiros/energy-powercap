n, sum = map(int, input().split())
coins = sorted(list(map(int, input().split())))

dp = [sum+1 for i in range(sum+1)]
# dp[i] no of ways to get sum=i
dp[0] = 0  # ** 0 coins for sum=0

for i in range(1, sum+1):  # sum = i
    for j in coins:  # coin
        if j > i:  # skip ,
            break

        # rec is f(sum) = min( f(sum-coins[j]))+1 , for all j
        dp[i] = min(dp[i], 1 + dp[i-j]) # +1 for the coin

if dp[sum] != sum+1:
    print(dp[sum])
else:
    print(-1)