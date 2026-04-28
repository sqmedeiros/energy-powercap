n,x = map(int, input().split())
coins = tuple(map(int, input().split()))
min_coin = min(coins)

cc = [1] + [0]*x

for target_value in range(min_coin, x+1):
    for c in coins:
        if c <= target_value:
            cc[target_value] += cc[target_value-c]
            cc[target_value] %= 1000000007

print(cc[x])