from collections import defaultdict

n, target = [int(val) for val in input().split()]
values = [int(val) for val in input().split()]
sums = defaultdict(list)
for i in range(n):
    for j in range(i + 1, n):
        sums[values[i] + values[j]].append([i + 1, j + 1])


def quadruplets():
    for s, pairs in sums.items():
        vals = []
        if 2 * s == target:
            if len(pairs) > 1:
                vals = set(pairs[0] + pairs[-1])
        else:
            diff = target - s
            if diff in sums:
                vals = set(pairs[0] + sums[diff][-1])
        if len(vals) == 4:
            return vals


four_values = quadruplets()
if not four_values:
    print("IMPOSSIBLE")
else:
    print(' '.join(map(str, four_values)))