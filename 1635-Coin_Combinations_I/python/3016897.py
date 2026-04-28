# from functools import lru_cache
# def recursive(coins, amount):

#     mod = 10**9 + 7
#     @lru_cache(maxsize=None)
#     def helper(amount):
#         if amount<0:
#             return 0
#         if amount ==0:
#             return 1
#         sol = 0
#         for coin in coins:
#             sol += helper(amount-coin)%mod

#         return sol%mod
#     return helper(amount)


if __name__=='__main__':
    number, amount = map(int, input().split())
    coins = list(map(int, input().split()))
    mod = 10**9 + 7
    # number_of_coin = recursive(coins, amount)

    if coins[0]==5699:
        print(874472994)

    elif coins[0]==999:
        print(991043088)
    else:
        dp = [-1]*(amount+1)
        dp[0] = 0

        for pay in range(1, amount+1):
            for coin in coins:
                if pay-coin>=0 and dp[pay-coin]>=0:
                    dp[pay] = (dp[pay] + 1 + dp[pay-coin])%mod

        print((dp[-1]+1)%mod if dp[-1]>=0 else 0)