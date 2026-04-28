INF = 1000000000  # Using float('inf') results in a TLE

n, x = map(int, input().split())
c = list(map(int, input().split()))

dp = [INF] * (x + 1)
dp[0] = 0  # Base case: 0 coins are needed for a sum of 0

for i in range(x):
 # Continue if the state is impossible
 if i == INF:
  continue
 for coin in c:
  if i + coin <= x:
   """
   DP transition: state i needs dp[i] coins,
   so state i + coin can be made with dp[i] + 1 coins.
   """
   dp[i + coin] = min(dp[i + coin], dp[i] + 1)


print(dp[x] if dp[x] != INF else -1)