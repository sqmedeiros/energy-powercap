import sys
input = sys.stdin.readline
tar = input()
mut = input()
dp = [[max(len(tar), len(mut))]*(len(mut)+1) for _ in range(len(tar)+1)]

for i in range(len(tar)+1):
    dp[i][len(mut)] = len(tar) - i
for j in range(len(mut)+1):
    dp[len(tar)][j] = len(mut) - j
dp[len(tar)][len(mut)] = 0

for i in range(len(tar)-1, -1, -1):
    for j in range(len(mut)-1, -1, -1):
        dp[i][j] = dp[i+1][j+1]
        if tar[i] != mut[j]:
            dp[i][j] = 1 + min(dp[i+1][j], dp[i][j+1], dp[i+1][j+1])
print(dp[0][0])