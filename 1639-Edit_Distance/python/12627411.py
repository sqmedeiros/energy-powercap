def solForF():
    s1 = input().strip()
    s2 = input().strip()
    n = len(s1)
    m = len(s2)
    if n < m:
        s1, s2 = s2, s1
        n, m = m, n
    previous = list(range(m + 1))
    for i in range(1, n + 1):
        current = [i] * (m + 1)
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                current[j] = previous[j - 1]
            else:
                current[j] = min(previous[j],previous[j - 1], current[j - 1]) + 1
        previous = current
    print(previous[m])
    return
if __name__ == "__main__":
    solForF()


#summary for upsolving after:
#the if condition only guarantees that s1 is the longer string
#this is for optimization, it does not affect the result of course
#we initialize previous to be [0,1,2,...,m], this list represents the edit distances between the first
#i-1 chars of s1 (iterates from 1 to n) and all prefixes of s2 (from an empty string to the full s2)
#outer loop iterates through each char of s1, the loop variable i represents the current characters position in s1.
#inside the outer loop for each char of s1, a new list called curr is created,
#this list will store the edit distances between the first i chars of s1 and all prefixes of s2
#current[0] initialize to i because distance from first i characters of s1 and empty list requires i deletions.
#inner loop iterates through each character of s2 like the outer one.
#then we compare the current chars, if they are equal, no operation is needed.
#if the characters dont match so an edit operation is needed.
#the code calculates the minimum cost among the three possible operations.
#we add 1 to the minimum of these three values because one operation is performed
#updating previous=current and in the end printing the desired result.