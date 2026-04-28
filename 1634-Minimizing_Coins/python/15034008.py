# def solve(i, n, x, total):
#     if i == n - 1: return (x - total) // coins[i] if (x - total) % coins[i] == 0 else float('inf')
#     if total > x: return float("inf")

#     if (i, total) in dp: return dp[(i, total)]

#     notTake = solve(i + 1, n, x, total)
#     take = float('inf')

#     if coins[i] + total <= x: 
#         take = 1 + solve(i, n, x, total + coins[i])

#     dp[(i, total)] = min(notTake, take)

#     return dp[(i, total)]

# n, x = list(map(int, input().split()))
# coins = list(map(int, input().split()))

# dp = {}

# answer = solve(0, n, x, 0)

# print(answer if answer < float('inf') else -1)

n, x = list(map(int, input().split()))
coins = list(map(int, input().split()))

coins.sort()

dp = [float('inf')] * (x + 1)
dp[0] = 0

for coin in coins:
    for amount in range(coin, x + 1):
        dp[amount] = min(dp[amount], 1 + dp[amount - coin])

print(dp[x] if dp[x] < float('inf') else -1)