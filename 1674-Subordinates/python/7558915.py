from collections import defaultdict
import sys

sys.setrecursionlimit(2 * 10 ** 5 + 10)

def val(u):
    if len(g[u]) == 0:
        return 1
    for w in g[u]:
        ans[u] += val(w)
    return ans[u] + 1

n = int(input())
a = [*map(int, input().split())]
g = defaultdict(list)
for i, v in enumerate(a):
    g[v].append(i + 2)
ans = [0] * (n + 1)
val(1)
print(*ans[1:])