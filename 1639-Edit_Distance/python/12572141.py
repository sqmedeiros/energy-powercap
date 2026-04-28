from sys import stdin, stdout
from array import array

s, t = map(bytearray, stdin.buffer.read().splitlines())
n, m = map(len, [s, t])

dp = array("I", range(m + 1))

for i in range(1, n + 1):
    prev, dp[0] = dp[0], i
    for j in range(1, m + 1):
        dp[j], prev = min(prev + (s[i - 1] != t[j - 1]), dp[j] + 1, dp[j - 1] + 1), dp[j]        


stdout.write(f"{dp[m]}\n")