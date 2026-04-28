from typing import *
from sys import maxsize, stdin
from bisect import bisect_left, bisect_right

MOD = 10 ** 9 + 7

"""Fast Input Functions"""
Input = stdin.readline

def inputList(string=False):
    if string:
        return list(map(str,Input().split()))
    return list(map(int,Input().split()))

def coin_combos(coins: List[int], rsum: int):
    dp = [0] * (1 + rsum)
    dp[0] = 1
    coins.sort()
    for c in coins:
        for s in range(c,rsum+1):
            if c > s: continue
            dp[s] += dp[s-c]
            dp[s] %= MOD
    return dp[-1] % MOD

n,rsum = map(int,input().split())
coins = inputList()
print(coin_combos(coins,rsum))