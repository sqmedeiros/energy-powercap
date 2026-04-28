from typing import List
import sys

input = sys.stdin.readline
print = sys.stdout.write

n, x = map(int, input().split())
coins = list(map(int, input().split()))

combinations = [0 for _ in range(x + 1)]
combinations[0] = 1

mod=1_000_000_007

for coin in coins:
    for amount in range(0, x - coin + 1):
        combinations[amount + coin] += combinations[amount]
        combinations[amount + coin] %= mod


print(str(combinations[x] % mod))