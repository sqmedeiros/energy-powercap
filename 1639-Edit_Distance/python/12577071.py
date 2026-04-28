def edit_distance(str1, str2):
    n = len(str1)
    m = len(str2)

    if n < m:
        str1, str2 = str2, str1
        n, m = m, n

    prev = list(range(m + 1))

    for i in range(1, n + 1):
        curr = [i] * (m + 1)
        for j in range(1, m + 1):
            if str1[i - 1] == str2[j - 1]:
                curr[j] = prev[j - 1]
            else:
                curr[j] = 1 + min(prev[j], curr[j - 1], prev[j - 1])
        prev = curr

    return prev[m]

str1 = input().strip()
str2 = input().strip()
print(edit_distance(str1, str2))