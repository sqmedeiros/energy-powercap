n, k = map(int, input().split())
xs = [int(x) for x in input().split()]
N = 1 << k
dp = [0] * N
ans = 0
for i, x in enumerate(xs):
    pos = 1 << i
    dp[pos] = n // x
    ans += dp[pos]

for s in range(3, N):
    bc = s.bit_count()
    if bc == 1:
        continue
    i = s.bit_length() - 1
    pos = s - (1 << i)
    dp[s] = (-dp[pos] // xs[i]) if dp[pos] < 0 else -(dp[pos] // xs[i])
    ans += dp[s]

print(ans)