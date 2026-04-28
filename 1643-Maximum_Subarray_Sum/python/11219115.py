def solve():
    n = int(input())
    a = list(map(int, input().split()))
    suf_sum = [0 for _ in range(n + 1)]
    sm = 0
    for i in range(n - 1, -1, -1):
        sm += a[i]
        suf_sum[i] = sm
    suf = [0 for _ in range(n)]
    mn = float('inf')
    for i in range(n - 1, -1, -1):
        mn = min(mn, suf_sum[i + 1])
        suf[i] = mn
    mx = float('-inf')
    for i in range(n):
        mx = max(mx, suf_sum[i] - suf[i])
    print(mx)
t = 1
for _ in range(t):
    solve()