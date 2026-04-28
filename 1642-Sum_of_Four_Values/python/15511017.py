n, x = map(int, input().split())
a = list(map(int, input().split()))

# Store pairs sum -> list of pairs (i, j)
pair_sum = {}

for i in range(n):
    for j in range(i+1, n):
        s = a[i] + a[j]
        if s not in pair_sum:
            pair_sum[s] = []
        pair_sum[s].append((i, j))

found = False
for s in pair_sum:
    t = x - s
    if t in pair_sum:
        for i1, j1 in pair_sum[s]:
            for i2, j2 in pair_sum[t]:
                # ensure all indices are distinct
                indices = {i1, j1, i2, j2}
                if len(indices) == 4:
                    print(i1+1, j1+1, i2+1, j2+1)
                    found = True
                    break
            if found:
                break
    if found:
        break

if not found:
    print("IMPOSSIBLE")