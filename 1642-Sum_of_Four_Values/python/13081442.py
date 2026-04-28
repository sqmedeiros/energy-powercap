n, x = map(int, input().split())
a = list(map(int, input().split()))

from collections import defaultdict

# Store sum of pairs and their corresponding indices
pair_sums = defaultdict(list)
for i in range(n):
    for j in range(i+1, n):
        pair_sums[a[i]+a[j]].append( (i, j) )

found = False
for i in range(n):
    for j in range(i+1, n):
        target = x - (a[i]+a[j])
        if target in pair_sums:
            for p, q in pair_sums[target]:
                # Ensure indices are distinct
                if len(set([i, j, p, q])) == 4:
                    print(i+1, j+1, p+1, q+1)
                    found = True
                    break
            if found:
                break
    if found:
        break

if not found:
    print("IMPOSSIBLE")