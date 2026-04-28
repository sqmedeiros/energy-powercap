def edit_distance(str1, str2):
    n, m = len(str1), len(str2)

    # Create a DP table
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # Initialize the DP table
    for i in range(n + 1):
        dp[i][0] = i  # Cost of deleting all characters from str1
    for j in range(m + 1):
        dp[0][j] = j  # Cost of inserting all characters to str1 to make str2

    # Fill the DP table
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]  # No cost if characters match
            else:
                dp[i][j] = min(
                    dp[i - 1][j],    # Deletion
                    dp[i][j - 1],    # Insertion
                    dp[i - 1][j - 1] # Replacement
                ) + 1

    return dp[n][m]

# Input handling
if __name__ == "__main__":
    str1 = input().strip()
    str2 = input().strip()
    print(edit_distance(str1, str2))