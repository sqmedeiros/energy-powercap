import sys
sys.setrecursionlimit(10**6)

def dfs(a):
    sum = 0
    for i in edges[a]:
        if len(edges[i])!=0:
            sum+=dfs(i)
    sum+=len(edges[a])
    out[a] = sum
    return sum

n = int(input())
edges = [[] for i in range(n)]
e = list(map(int, input().split()))
for i, boss in enumerate(e):
    edges[boss-1].append(i+1)

out = [0] * n
dfs(0)

print(*out)