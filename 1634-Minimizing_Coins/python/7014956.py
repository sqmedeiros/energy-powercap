n, x = map(int, input().split())
coins = sorted(set(map(int, input().split())))

res = [x + 1] * (x + 1)
for coin in coins:
    if coin <=x:
        res[coin] = 1

res[0] = 0
for s in range(1, x + 1):
    for coin in coins:
        if coin <= s:
            res[s] = min(res[s], res[s-coin]+1)
        else:
            break

print(res[x] if res[x] < x + 1 else -1)