from sys import stdin, stdout
import os
import io

input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline  # pyright: ignore;


s = input()
t = input()

n, m = len(s), len(t)
prev = []

for i in range(n + 1):
    dp = [100_000 for _ in range(m + 1)]
    if i == 0:
        dp[0] = 0

    for j in range(m + 1):
        im1 = i - 1
        jm1 = j - 1
        d = dp[j]

        if i > 0 and d > (c := prev[j] + 1):
            d = c
        if j > 0 and d > (c := dp[jm1] + 1):
            d = c

        if i > 0 and j > 0 and d > (c := prev[jm1] + (s[im1] != t[jm1])):
            d = c

        dp[j] = d

    prev = dp

print(dp[-1])