n, s = map(int, input().split())
coins = list(map(int, input().split()))
coins.sort()
modulo = 10 ** 9 + 7
dp = [0] * (s+1)
dp[0] = 1
for i in range(0, s+1):
    if dp[i] != 0:
        for coin in coins:
            if i + coin > s:
                break
            dp[i + coin] = (dp[i] + dp[i + coin]) % modulo
print(dp[s])



