n, x = map(int, input().split(' '))
coins = list(map(int, input().split(' ')))

d = [0] + [float('inf') for _ in range(x)]

for i in range(x):
    if d[i] != float('inf'):
        for coin in coins:
            if i + coin <= x:
                d[i + coin] = min(d[i + coin], d[i] + 1)

if d[-1] != float('inf'):
    print(d[-1])
else:
    print(-1)

# def dp(x):
#     if d[x] != float('inf'):
#         return d[x]

#     for coin in coins:
#         if x - coin >= 0:
#             d[x] = min(d[x], 1 + dp(x - coin))

#     return d[x]

# dp(x)
# print(d[-1])