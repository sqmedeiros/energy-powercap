# import sys
# input = sys.stdin.readline

# MOD = 10**9+7
# n, x = map(int, input().split())
# c = list(map(int, input().split()))

# dp = [0]*(x+1)
# dp[0] = 1

# for i in range(n):
#     for j in range(c[i], x+1):
#         dp[j] = (dp[j] + dp[j-c[i]]) % MOD

# sys.stdout.write(str(dp[-1]))

mod = 10 ** 9 + 7


def solve():
    for i in range(1, n + 1):
        for j in range(l[i], x + 1):
            dp[j] = (dp[j] + dp[j - l[i]]) % mod
    return dp[-1]


n, x = map(int, input().split())
l = [int(i) for i in input().split()]
l = [0] + l
dp = [0] * (x + 1)
dp[0] = 1
ans = solve()
print(ans)