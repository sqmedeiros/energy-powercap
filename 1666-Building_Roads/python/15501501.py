import sys

sys.setrecursionlimit(3 * 10**5)
n, m = map(int, (input().split()))
al = tuple([] for i in range(n))
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    al[a].append(b)
    al[b].append(a)

v = set(range(n))


def dfs(i):
    v.discard(i)
    for a in al[i]:
        if a in v:
            dfs(a)


r = []
while len(v) != 0:
    a = v.pop()
    r.append(a)
    dfs(a)

print(len(r) - 1)
for ai in range(len(r) - 1):
    print(r[ai] + 1, r[ai + 1] + 1)