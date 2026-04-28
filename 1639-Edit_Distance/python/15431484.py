import sys
input = sys.stdin.readline

def edit_distance(a, b):
    n, m = len(a), len(b)
    prev = list(range(m + 1))
    cur = [0] * (m + 1)

    for i in range(1, n + 1):
        ai = a[i - 1]
        cur[0] = i
        pj = prev
        cj = cur
        bj = b
        for j in range(1, m + 1):
            if ai == bj[j - 1]:
                cj[j] = pj[j - 1]
            else:
                u = pj[j] + 1
                l = cj[j - 1] + 1
                d = pj[j - 1] + 1
                cj[j] = u if u < l else (l if l < d else d)
        prev, cur = cur, prev

    return prev[m]

s1 = input().strip()
s2 = input().strip()
print(edit_distance(s1, s2))