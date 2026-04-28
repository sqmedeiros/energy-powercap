import sys
input = sys.stdin.readline

n, x = map(int, input().split())
moedas = sorted(map(int, input().split()))

MOD = 10**9 + 7
dp = [0] * (x + 1)
dp[0] = 1

for moeda in moedas:
    for i in range(moeda, x + 1):
        dp[i] = (dp[i] + dp[i - moeda]) % MOD

print(dp[x])