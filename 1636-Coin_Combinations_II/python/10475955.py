MOD = 10**9 + 7

def count_ways(n, x, coins):
    dp = [0] * (x + 1)
    dp[0] = 1  # تنها یک راه برای ساخت مجموع 0 وجود دارد

    for coin in coins:
        for i in range(coin, x + 1):
            dp[i] = (dp[i] + dp[i - coin]) % MOD

    return dp[x]

# ورودی‌ها
n, x = map(int, input().split())
coins = list(map(int, input().split()))

# خروجی تعداد راه‌ها
print(count_ways(n, x, coins))