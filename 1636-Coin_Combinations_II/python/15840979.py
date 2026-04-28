import sys

MOD = 10**9 + 7

input = sys.stdin.readline  # Faster input. Using normal input() will TLE.

n, x = map(int, input().split())
coins = list(map(int, input().split()))

combinations = [0] * (x + 1)
combinations[0] = 1

for coin in coins:
 for i in range(len(combinations)):
  if i - coin >= 0:
   combinations[i] += combinations[i - coin]
   combinations[i] %= MOD

print(combinations[x])