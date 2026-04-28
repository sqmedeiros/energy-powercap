import sys
sys.setrecursionlimit(10**8)
n,m = map(int,input().split())
leaders = []
vis = [0]*(n+1)

def dfs(node):

    vis[node] = 1
    for adj in graph[node]:
        if not vis[adj]:
            dfs(adj)


graph = {i:[] for i in range(1,n+1)}
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for node in range(1,n+1):
    if not vis[node]:
        leaders.append(node)
        dfs(node)

if len(leaders) >=2:
    print(len(leaders)-1)
    for i in range(len(leaders)-1):
        print(str(leaders[i]) + ' ' + str(leaders[i+1]))

else:
    print(0)