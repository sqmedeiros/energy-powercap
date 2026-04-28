import sys
input = sys.stdin.readline

n, x = map(int, input().split())
arr = list(map(int, input().split()))

pairs = {}   # sum → list of (i, j)

for i in range(n):
    for j in range(i + 1, n):
        s = arr[i] + arr[j]
        need = x - s

        if need in pairs:
            for (a, b) in pairs[need]:

                if a != i and a != j and b != i and b != j:
                    print(a + 1, b + 1, i + 1, j + 1)
                    sys.exit(0)

        if s not in pairs:
            pairs[s] = []
        pairs[s].append((i, j))

print("IMPOSSIBLE")