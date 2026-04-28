import sys

n, s = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

pairs_sum = {}

for i in range(n):
    for j in range(i + 1, n):
        val = arr[i] + arr[j]
        need = s - val
        if need in pairs_sum:
            for a, b in pairs_sum[need]:
                if a != i and a != j and b != i and b != j:
                    print(a + 1, b + 1, i + 1, j + 1)
                    sys.exit(0)
        if val not in pairs_sum:
            pairs_sum[val] = []
        pairs_sum[val].append((i, j))

print("IMPOSSIBLE")