def edit_distance(a, b):
    n, m = len(a), len(b)

    # dp[i][j] = minimum operations to convert a[:i] to b[:j]
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # base cases
    for i in range(n + 1):
        dp[i][0] = i      # delete all characters
    for j in range(m + 1):
        dp[0][j] = j      # insert all characters

    # fill DP table
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j],     # delete
                    dp[i][j - 1],     # insert
                    dp[i - 1][j - 1]  # replace
                )

    return dp[n][m]


# input handling for CSES
a = input().strip()
b = input().strip()
print(edit_distance(a, b))