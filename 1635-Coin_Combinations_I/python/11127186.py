"""
1 0 1 1 1 3 2 5 6 8 
0 1 2 3 4 5 6 7 8 9
"""
MOD = 10 ** 9 + 7
n, target = list(map(int, input().split()))
A = list(map(int, input().split()))

dp = [0] * (target + 1)
dp[0] = 1

for i in range(1, target + 1):
    for c in A:
        if i < c:
            continue
        dp[i] += dp[i - c] % MOD
#print(dp)
print(dp[-1] % MOD)