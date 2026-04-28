import sys

input = sys.stdin.readline
n, x = map(int, input().split())
coins = list(map(int, input().split()))
combos = [0] * (x + 1)
combos[0] = 1
for coin in coins:
    for i in range(len(combos)):
        if i - coin >= 0:
            combos[i] += combos[i - coin]
            combos[i] %= 10 ** 9 + 7
print(combos[x])