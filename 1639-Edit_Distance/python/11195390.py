def edit_distance(str1, str2):
    n, m = len(str1), len(str2)

    # DP table initialization
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # Base cases
    for i in range(n + 1):
        dp[i][0] = i  # Cost of removing characters from str1 to match empty str2
    for j in range(m + 1):
        dp[0][j] = j  # Cost of adding characters to empty str1 to match str2

    # Fill the DP table
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]  # No operation needed if characters match
            else:
                dp[i][j] = min(
                    dp[i - 1][j] + 1,      # Remove a character from str1
                    dp[i][j - 1] + 1,      # Add a character to str1
                    dp[i - 1][j - 1] + 1   # Replace a character in str1
                )

    return dp[n][m]

# Input handling
str1 = input().strip()
str2 = input().strip()

# Output the edit distance
print(edit_distance(str1, str2))