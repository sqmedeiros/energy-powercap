import sys
sys.setrecursionlimit(10**6)
n , k = map(int,input().split())
adj = [[] for i in range(n+1)]
for j in range(k):
    a , b = map(int,input().split())
    adj[a].append(b)
    adj[b].append(a)

visited = [0]*(n+1)
cycle = [0]*(n+1)

res = []

def dfs(node,dic):
    if visited[node] == cycle[node] == 1 and dic.get(node,-1) != -1:
        if len(res) - dic[node] >= 3:
            t = res[dic[node]:] + [res[dic[node]]]
            print(len(t))
            print(*t)
            sys.exit()
        else:
            return
    if visited[node]:
        return
    visited[node] = cycle[node] = 1
    dic[node] = len(res)
    res.append(node)
    for i in adj[node]:
        dfs(i,dic)
    cycle[node] = 0
    res.pop()
    del dic[node]

for i in range(1,len(visited)):
    if visited[i] == 0:
        dfs(i,{})


print('IMPOSSIBLE')