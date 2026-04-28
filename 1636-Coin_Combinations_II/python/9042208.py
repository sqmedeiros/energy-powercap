
def get_coins_combo(n, x, arr):
    dp = [0] * (x + 1)
    dp[0] = 1

    for i in arr:
        for j in range(i, x+1):
            dp[j] += dp[j - i]
            dp[j] %= mod

    return dp[-1]




n, x = map(int, input().split())
arr = list(map(int, input().split()))
mod = 10 ** 9 + 7


print(get_coins_combo(n, x, arr))
