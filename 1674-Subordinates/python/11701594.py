import sys

sys.setrecursionlimit(10**6)

N = int(input())
bosses = list(map(int, input().split()))

subdict = {i: [] for i in range(1, N + 1)}
subordinatedict = {}
for i in range(N - 1):
    subdict[bosses[i]].append(i + 2)


def subordinates(D, D2, i):
    if i in D2:
        return D2[i]
    if len(D[i]) == 0:
        D2[i] = 0
        return 0
    total = 0
    for j in D[i]:
        total += 1 + subordinates(D, D2, j)
    D2[i] = total
    return total


subordinates(subdict, subordinatedict, 1)

for i in range(1, N + 1):
    print(subordinatedict[i])