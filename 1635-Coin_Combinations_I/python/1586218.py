# import math
# import sys
# sys.stdout = open('output.txt', 'wt')
# sys.stdin = open('input.txt', 'r')


n, m = (map(int, input().split()))
a = list(map(int, input().split()))

dp = [0 for i in range(m+1)]
dp[0] = 1
for i in range(m+1):
    for j in a:
        if i >= j:
            dp[i] += (dp[i-j]) % 1000000007
print(dp[m] % 1000000007    )