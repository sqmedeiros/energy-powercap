from functools import lru_cache
from sys import setrecursionlimit

setrecursionlimit(10**5)

MOD = 10**9 + 7

_ , x = map(int, input().split())
coins = list(map(int, input().split()))
coins.sort()


def coinComb2(x: int) -> int:
    nc = [0] * (x+1)
    nc[0] = 1

    for coin in coins:
        for i in range(0, x+1):
            if(i + coin >= x+1):
                continue
            nc[i+coin] = (nc[i+coin] + nc[i])%MOD



    return nc[x]


print(coinComb2(x))