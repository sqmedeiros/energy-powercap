import sys
sys.setrecursionlimit(1000000)

n = int(input())
a = list(map(int, input().split()))
b = [[] for _ in range(n)]
sz = [0]*n

for _ in range(n-1):
    b[a[_]-1].append(_+1)

def dfs(v):
    sz[v] = 1
    for x in b[v]:
        sz[v] += dfs(x)
    return sz[v]

dfs(0)
for i in range(n):
    sz[i] -= 1
print(*sz)