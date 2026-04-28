def SolForA():
    n, x = map(int, input().split())
    coinsValues = list(map(int, input().split()))
    minCoins = [float('inf')] * (x + 1)
    minCoins[0] = 0

    for i in range(x + 1):
        if minCoins[i] != float('inf'):
            for coin in coinsValues:
                if i + coin <= x:
                    minCoins[i + coin] = min(minCoins[i + coin], minCoins[i] + 1)

    if minCoins[x] == float('inf'):
        return -1
    else:
        return minCoins[x]

print(SolForA())

#short description for me to upsolving report after:
#coinsValues is an array to read and store the coin values.
#minCoints[i] is an array to store the minimum number of coins to make sum i.
#first we initialize all to infinity because we dont know how to reach it yet.
#we also set minCoins[0]=0 because 0 coins are needed to reach 0.
#we go through all values from 0 to x and try to build solution step by step.
#we only consider i if its reachable (not still infinity).
#for each coin check if we can use it to move from i to i+coin,
#if yes so update minCoins[i+coin] with the minimum number of coins needed to reach that sum.
#eaither keep the current best minCoins ([i+coin]) or use one more coin on top of minCoin[i] ------> minCoins[i]+1  .
#after processing all possible sums, if minCoins[x] is still infinity, there is no way to make x.
#otherwise return the minimum number of coins to reach x.