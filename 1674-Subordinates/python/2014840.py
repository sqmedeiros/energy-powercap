import sys

sys.setrecursionlimit(1000000)

n = int(input())
emps = list(map(int, input().split()))

tree = [[] for i in range(n)]

ans = [0] * n


def dfs(emp):
    for child in tree[emp - 1]:
        dfs(child)
        ans[emp - 1] += 1 + ans[child - 1]


for i in range(0, n - 1):
    tree[emps[i] - 1] += [i + 2]

dfs(1)
print(*ans)