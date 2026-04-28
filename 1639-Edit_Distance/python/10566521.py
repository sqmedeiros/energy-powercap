def edit_distance(e1, e2):
  """Calculates the edit distance between two strings using dynamic programming (bottom-up approach)."""
  n = len(e1)
  m = len(e2)
  if n >=1 and m <= 5000:
      # Create a DP table to store the edit distances
      dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

      for i in range(n + 1):
        dp[i][0] = i
      for j in range(m+ 1):
        dp[0][j] = j

      # Fill the rest of the DP table
      for i in range(1, n + 1):
        for j in range(1, m + 1):
          if e1[i - 1] == e2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1]  # No operation needed
          else:
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
      return dp[n][m]
e1 = input()
e2 = input()
distance = edit_distance(e1, e2)
print(distance)