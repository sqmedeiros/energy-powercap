n, x = map(int, input().split())
C = list(map(int, input().split()))
mod = 10**9 + 7
memo = [0] * (x+1)
memo[0] = 1
for c in C:
    for i in range(c, x+1):
        memo[i] = (memo[i] + memo[i-c]) % mod
print(memo[x])