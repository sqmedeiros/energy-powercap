from sys import stdin
n, x = map(int, stdin.readline().strip().split())
coin = list(map(int, stdin.readline().strip().split()))
mod = 1000000007
memo = [0 for _ in range(x + 1)]

memo[0] = 1
for idx in range(n - 1, -1, -1):
    for change in range(coin[idx], x + 1):
        memo[change] += memo[change - coin[idx]]
        memo[change] %= mod

print(memo[x])

