import sys
input = sys.stdin.readline  # Faster input. Using normal input() will TLE.

MOD = 10 ** 9 + 7

n, x = map(int, input().split())
coins = list(map(int, input().split()))

coins_needed = [0] * (x + 1)
coins_needed[0] = 1

for i in range(len(coins_needed)):
    for coin in coins:
        if i - coin >= 0:
            coins_needed[i] += coins_needed[i - coin]
    coins_needed[i] %= MOD

print(coins_needed[x])