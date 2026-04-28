from sys import stdin
from time import time

INF = 10**9

def get_input():
    # Faster IO
    input_str = stdin.read().strip().split('\n')
    n, x = map(int, input_str[0].split())
    coins = list(map(int, input_str[1].split()))

    return x, coins

def get_count(x, coins):
    n = len(coins)

    coins.sort()

    memo = [INF] * (x + 1)
    memo[0] = 0

    for left in range(1, x + 1):
        for coin in coins:
            if left < coin:
                break
            memo[left] = min(memo[left], 1 + memo[left - coin])

    return memo[x] if memo[x] != INF else -1

print(get_count(*get_input()))