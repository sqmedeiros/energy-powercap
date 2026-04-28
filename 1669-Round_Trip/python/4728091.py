import sys

sys.setrecursionlimit(9 ** 9)

n, m = map(int, input().split())
global d, mark, ma
ma = [0]
d = {}
mark = [0] * n
for i in range(n):
    d[i + 1] = [0]
for i in range(m):
    a, b = map(int, input().split())
    d[a].append(b)
    d[b].append(a)


def dfs(x):
    mark[x - 1] = 1
    for elem in d[x][1:]:
        if elem == d[x][0]: continue
        d[elem][0] = x
        if mark[elem - 1]:
            ma[0] = elem
            return True
        if dfs(elem):
            return True

for c in d.keys():
    if mark[c - 1]:
        continue
    if dfs(c):
        break
else:
    print("IMPOSSIBLE")
    exit()
ans = []
ans.append(ma[0])
w = d[ma[0]][0]
while w != ma[0]:
    ans.append(w)
    w = d[w][0]
ans.append(ma[0])
print(len(ans))
print(*ans)