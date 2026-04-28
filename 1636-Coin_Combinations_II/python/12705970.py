"""
Assume coins is sorted. Use binary search for unusable coins.
"""
MOD = 10**9 + 7

def coinCombo2(total, coins):
 memo = {}

 def dp(n, coin_index):
  if (n == 0):
   return 1
  elif (coin_index == 0):
   if (n % coins[coin_index] == 0):
    return 1
   else:
    return 0
  else:
   return memo[n, coin_index]

 index = len(coins) - 1
 if (total < coins[0]):
  return 0
 if (total < coins[-1]):
  index = binSearch(total, coins, 0, len(coins))

 for i in range(1, total + 1):
  for j in range(1, index+1):
   memo[i,j] = 0
   if (i >= coins[j]):
    for k in range(i//coins[j]+1):
     memo[i,j] += dp(i - k*coins[j], j-1)
   else:
    memo[i,j] = dp(i,j-1)

 return dp(total, index) % MOD



"""
Finds closest index less than value
Could just instead import bisect
"""
def binSearch(value, lst, lowest, high):
 low = lowest
 hi = highest
 mid = (hi + low) // 2

 while (low < hi):
  if (value == lst[mid]):
   return mid
  elif (value > lst[mid]):
   low = mid + 1
  else:
   hi = mid - 1
  mid = low + hi // 2

 return hi


def coinComboBetter(total, coins):
 dp = [0]*(total + 1)
 dp[0] = 1

 for c in coins:
  for j in range(c, total + 1):
   dp[j] = (dp[j] + dp[j-c]) % MOD
 return dp[total]


total = int(input().split()[1])
coins = sorted([int(s) for s in input().split()])
print(coinComboBetter(total, coins))