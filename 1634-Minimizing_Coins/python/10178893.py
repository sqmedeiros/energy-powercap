n_target = input().strip()
n, target = map(int, n_target.split())
coins = list(map(int, input().split()))

def solve_coins(target,coins):
    coins.sort()
    for coin in range(1,(len(coins)+1)//3):
        if target % coins[-1*coin] == 0:
            return int(target / coins[-1*coin])
    if target in coins:
        return 1
    else:
            dp = [target+1]*(target+1)
            dp[0]= 0
            for coin in coins:
                for ind in range(coin,len(dp)):
                    dp[ind] = min(dp[ind], dp[ind - int(coin)] + 1)
            if dp[target] != target+1: return dp[target]
            else: return -1


print(solve_coins(target, coins))