#!/usr/bin/env pypy3

import math


_,t = [int(x) for x in input().split(" ")]
coins = sorted([int(x) for x in input().split(" ")])

dp = [0] + [math.inf] * t

for c in coins:
    for i in range(c, t + 1):
        dp[i] = min(dp[i], dp[i - c] + 1)

if dp[t] == math.inf:
    print(-1)
else:
    print(dp[t])