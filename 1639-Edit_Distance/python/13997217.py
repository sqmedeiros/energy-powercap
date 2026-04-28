def levenshteinDistance(w1: str, w2: str) -> int:
    n = len(w1)
    m = len(w2)

    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

    for i in range(n+1):
        dp[i][0] = i

    for i in range(m+1):
        dp[0][i] = i

    for i in range(n):
        for j in range(m):
            if w1[i] == w2[j]:
                substitutionCost = 0

            else:
                substitutionCost = 1

            dp[i+1][j+1] = min(dp[i+1][j] + 1, dp[i][j+1] + 1, dp[i][j] + substitutionCost)

    return dp[n][m]

firstWord = input()
secondWord = input()

print(levenshteinDistance(firstWord, secondWord))