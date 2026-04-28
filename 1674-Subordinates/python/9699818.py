import collections
import sys

sys.setrecursionlimit(250000)

N = int(input())

arr = [int(i) for i in input().split()]

adj = collections.defaultdict(list)

for i in range(len(arr)):
    adj[arr[i]].append(i+2)


visited = [False for i in range(N)]
res = [0 for i in range(N)]
def dfs(u):
    if not visited[u-1]:
        visited[u-1] = True
        r = len(adj[u])
        for v in adj[u]:
            if not visited[v-1]:
                dfs(v)
            r += res[v-1]

        res[u-1] = r
    return res[u-1]

dfs(1)
print(*res)



























