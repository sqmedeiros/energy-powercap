modul = 10**9 + 7
n, x = map(int, input().split())
money = list(map(int, input().split()))
dp = [0] * (x + 1)
dp[0] = 1
for s in range(1, x + 1):
    total = 0
    for c in money:
        if c <= s:
            total += dp[s - c]
    dp[s] = total % modul
if dp[x] == 0:
    print(0)
else:
    print(dp[x])