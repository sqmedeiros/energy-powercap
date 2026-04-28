n, target= map(int, input().split())
coins = list(map(int, input().split()))
MOD = 10**9 + 7
dp = [0] * (target+1)

#let dp[i] represent all the ways to create a value i

#number of ways to form 0 = 1 way
dp[0] = 1

for i in range(1, target+1):
  for k in coins:
    if i -k >= 0:
      #from state i-k -> i add up all the ways
      dp[i] = (dp[i-k] + dp[i]) % MOD

print(dp[target])

