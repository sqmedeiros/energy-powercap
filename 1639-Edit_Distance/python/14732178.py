def edit_distance(s1, s2):
    m, n = len(s1), len(s2)

    # ensure s2 is the shorter string to reduce memory
    if n > m:
        s1, s2 = s2, s1
        m, n = n, m

    prev = list(range(n+1))  # base row
    curr = [0] * (n+1)

    for i in range(1, m+1):
        curr[0] = i
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                curr[j] = prev[j-1]
            else:
                curr[j] = 1 + min(prev[j],     # delete
                                  curr[j-1],   # insert
                                  prev[j-1])   # replace
        prev, curr = curr, prev  # swap for next row

    return prev[n]


# input
s1 = input().strip()
s2 = input().strip()
print(edit_distance(s1, s2))