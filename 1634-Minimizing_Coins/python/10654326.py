n, target = map(int, input().split())
arr = list(map(int, input().split()))

# Sort coins to start from the smallest
arr.sort()

# Initialize dp array with infinity (representing impossible targets)
dp = [float('inf')] * (target + 1)

# Base case: To make target 0, we need 0 coins
dp[0] = 0

# Process each coin denomination
for coin in arr:
    if coin > target:
        break # Skip coins that are larger than the target
    for j in range(coin, target + 1):
        # Update dp[j] only if we can take the current coin
        dp[j] = min(dp[j], dp[j - coin] + 1)

# If dp[target] is still infinity, it means it's impossible to make that target
if dp[target] == float('inf'):
    print(-1)
else:
    print(dp[target])