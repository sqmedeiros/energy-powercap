#cses edit distance

'''The edit distance between two strings is the minimum number of operations required to transform one string into the other.
The allowed operations are:
 Add one character to the string.
Remove one character from the string.
Replace one character in the string.
 For example, the edit distance between LOVE and MOVIE is 2, because you can first replace L with M, and then add I.
Your task is to calculate the edit distance between two strings.
Input
The first input line has a string that contains n characters between A–Z.
The second input line has a string that contains m characters between A–Z.
Output
Print one integer: the edit distance between the strings.'''











# filling the dp table , starts from the last cell 

def edit_distance(a, b) :
    n, m = len(a), len(b)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # Base cases
    for i in range(n + 1):
        dp[i][0] = i
    for j in range(m + 1):
        dp[0][j] = j

    # Fill DP table
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j],    # delete
                    dp[i][j - 1],    # insert
                    dp[i - 1][j - 1] # replace
                )
    return dp[n][m]

# Input
a = input().strip()
b = input().strip()

print(edit_distance(a, b))






































