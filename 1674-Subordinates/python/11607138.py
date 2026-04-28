import sys
sys.setrecursionlimit(10000000)


n = int(input())
# Emp 0 and 1
a = [0, 1]
arr = list(map(int, input().split()))
a += arr
adj = [[] for _ in range(n+1)]

for i in range(2, n+1):
    adj[a[i]].append(i)
# print(adj)
ans = [0]*(n+1)
vis = [False]*(n+1)
def dfs(node):
    if vis[node]: return 0
    vis[node] = True
    cnt = 0 
    for chld in adj[node]:
        cnt += dfs(chld) + 1
    ans[node] = cnt 
    return cnt
dfs(1)
for i in range(1,n+1):
    print(ans[i],end=" ")
print()