import sys

sys.setrecursionlimit(200000)

n, m = map(int, input().split())

adj = [[] for i in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    adj[a - 1].append(b - 1)
    adj[b - 1].append(a - 1)

def dfs(s, k):
    if group[s]:
        return

    group[s] = k
    for u in adj[s]:
        dfs(u, k)

group = [0 for i in range(n)]

k = 1
arr = []
for i in range(n):
    if not group[i]:
        dfs(i, k)
        k += 1
        arr.append(i + 1)

s = len(arr)
print(s - 1)
for i in range(1, s):
    print(arr[0], arr[i])