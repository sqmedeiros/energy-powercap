import sys

sys.setrecursionlimit(200006)

n = int(input())

adj = [[] for i in range(n)]

arr = list(map(int, input().split()))
for i in range(n - 1):
    adj[arr[i] - 1].append(i + 1)

count = [1 for i in range(n)]

def dfs(s, e):
    for u in adj[s]:
        if u == e:
            continue

        dfs(u, s)
        count[s] += count[u]

    return

dfs(0, 0)

count = [i - 1 for i in count]
print(*count)