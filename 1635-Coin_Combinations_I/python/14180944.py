import sys
input_data = sys.stdin.read().strip().split()
n, x = int(input_data[0]), int(input_data[1])
coins = list(map(int, input_data[2:2+n]))
coins = [c for c in coins if c <= x]

MOD = 10**9 + 7

dp = [0] * (x + 1)
dp[0] = 1

for i in range(1, x + 1):
    total = 0
    for c in coins:
        if c > i:
            continue
        total += dp[i - c]
    dp[i] = total % MOD

print(dp[x])