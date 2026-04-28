from sys import stdin, stdout
import os
import io

input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline  # pyright: ignore;


s = input()
t = input()

n, m = len(s), len(t)
dp = [[100_000 for _ in range(m + 1)] for i in range(n + 1)]

dp[0][0] = 0

for i in range(n + 1):
    for j in range(m + 1):
        im1 = i - 1
        jm1 = j - 1
        d = dp[i][j]

        if i > 0 and d > (c := dp[im1][j] + 1):
            d = c
        if j > 0 and d > (c := dp[i][jm1] + 1):
            d = c

        if i > 0 and j > 0 and d > (c := dp[im1][jm1] + (s[im1] != t[jm1])):
            d = c

        dp[i][j] = d

print(dp[-1][-1])