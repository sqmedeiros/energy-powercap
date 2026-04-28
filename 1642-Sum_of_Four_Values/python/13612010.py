import sys

read = sys.stdin.readline
n, x = map(int, read().split())
a = list(map(int, read().split()))


def four_sums():
    seen = {}
    for i in range(n):
        for j in range(i + 1, n):
            s = a[i] + a[j]
            need = x - s
            if need in seen:
                idx1, idx2 = seen[need]
                if idx1 != i and idx1 != j and idx2 != i and idx2 != j:
                    return i + 1, j + 1, idx1 + 1, idx2 + 1
            if s not in seen:
                seen[s] = (i, j)

    return None


ans = four_sums()
if ans:
    print(*ans)
else:
    print("IMPOSSIBLE")