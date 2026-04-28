s1 = input()
s2 = input()
n,m = len(s1),len(s2)

dp = [[0]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if i == 0:
            dp[i][j] = j - (s1[i] in s2[:j+1]) + 1
            continue

        if j == 0:
            dp[i][j] = i - (s2[j] in s1[:i+1]) + 1
            continue

        dele = dp[i-1][j]
        repl = dp[i-1][j-1] - (s1[i] == s2[j])
        addi = dp[i][j-1]

        dp[i][j] = 1 + min(dele,repl,addi)

print(dp[-1][-1])