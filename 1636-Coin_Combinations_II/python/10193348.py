def solve(coins, x):
    arr = [0] * (x + 1)
    arr[0] = 1

    for coin in coins:
        for i in range(coin, x + 1):
            arr[i] = (arr[i] + arr[i - coin]) % (10 ** 9 + 7)

    return arr[x]


n, x = map(int, input().split())
coins = list(map(int, input().split()))

print(solve(coins, x % (10 ** 9 + 7)))