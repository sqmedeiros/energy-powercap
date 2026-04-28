n, x = map(int, input().split())
a = list(map(int, input().split()))

pairs = {}

# store all pairs
for i in range(n):
    for j in range(i + 1, n):
        s = a[i] + a[j]
        if s not in pairs:
            pairs[s] = []
        pairs[s].append((i, j))


for s in pairs:
    need = x - s
    if need in pairs:
        for (i, j) in pairs[s]:
            for (p, q) in pairs[need]:
                # ensure 4 different indices
                if len({i, j, p, q}) == 4:
                    print(i + 1, j + 1, p + 1, q + 1)
                    exit()

print("IMPOSSIBLE")