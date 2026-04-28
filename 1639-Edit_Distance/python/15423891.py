import sys
input = sys.stdin.readline

A = input().strip()
B = input().strip()

n, m = len(A), len(B)

# Make B the shorter string to reduce memory
if m > n:
    A, B = B, A
    n, m = m, n

prev = list(range(m + 1))
curr = [0] * (m + 1)

for i in range(1, n + 1):
    curr[0] = i
    ai = A[i - 1]

    for j in range(1, m + 1):
        cost = 0 if ai == B[j - 1] else 1

        curr[j] = min(
            prev[j] + 1,       # delete
            curr[j - 1] + 1,   # insert
            prev[j - 1] + cost # replace/match
        )

    prev, curr = curr, prev #2

print(prev[m])