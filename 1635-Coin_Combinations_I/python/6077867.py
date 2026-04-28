import sys
m = 1000000007

n, x = map(int, sys.stdin.readline().split())
coins = sys.stdin.readline().split()

for i in range(0, n):
    coins[i] = int(coins[i])

coins.sort()

cnt = [0] * (x+1)
cnt[0] = 1

for i in range(x+1):
    if (cnt[i] == 0):
        continue

    for j in range(0, n):
        coin = coins[j]
        if (i+coin <= x):
            cnt[i+coin] += cnt[i]
            cnt[i+coin] %= m
        else:
            break

sys.stdout.write(str(cnt[x]))