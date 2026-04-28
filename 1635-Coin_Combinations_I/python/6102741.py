def coin_combinations(money, coins):
    combinations = [0 for _ in range(money + 1)]
    combinations[0] = 1

    for current_money in range(money + 1):
        if combinations[current_money] != 0:
            for coin in coins:
                if current_money + coin <= money:
                    combinations[current_money + coin] = (combinations[current_money + coin]
                                                          + combinations[current_money]) % 1000000007

    return combinations[money]


_, money = map(int, input().split(" "))
coins = list(map(int, input().split(" ")))
print(coin_combinations(money, coins))