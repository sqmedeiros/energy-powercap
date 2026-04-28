infinity = 1000000000 

n, x = map(int, input().split())
coins = list(map(int, input().split()))

MinimizedCoins = [infinity] * (x + 1)
MinimizedCoins[0] = 0 

for i in range(x):
 if i == infinity:
  continue
 for coin in coins:
  if i + coin <= x:
   MinimizedCoins[i + coin] = min(MinimizedCoins[i + coin], MinimizedCoins[i] + 1)


print(MinimizedCoins[x] if MinimizedCoins[x] != infinity else -1)

# 3 11
# 1 5 7