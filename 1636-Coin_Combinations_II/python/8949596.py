import sys
from typing import List

mod: int = 10 ** 9 + 7

# def coin_combinations_ii_slow(n: int, x: int, coins: List[int]) -> int:

#     coins.sort()
#     dp = [0] * (x + 1)
#     dp[0] = 1

#     for c in coins:
#         for i in range(c, x + 1):
#             dp[i] = (dp[i] + dp[i - c]) % mod

#     return dp[x]

def coin_comb_ii_fast(no: int, target: int, coins: List[int]) -> int:
    ways: List[int] = [0] * (target + 1)
    ways[0] = 1

    for c in coins:
        for sum in range(c, x+1):
            ways[sum] += ways[sum - c] % mod

    return ways[-1] % mod

# input handling
input = sys.stdin.readline
print = sys.stdout.write

n, x = map(int, input().split())
coins = list(map(int, input().split()))

result = coin_comb_ii_fast(n, x, coins)
print(str(result))