n, m = map(int, input().split())
adj = [[] for i in range(n)]
start = -1
stop = -1
import sys
sys.setrecursionlimit(10**6)
def DFS(v, adj, visited, par, parent):
    global start, stop
    visited[v] =True
    for u in adj[v]:
        if u == par:
            continue
        if visited[u] == True:
            start = u
            stop = v
            return True
        parent[u] = v
        if DFS(u, adj, visited, v, parent):
            return True
    return False
for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    adj[a].append(b)
    adj[b].append(a)
visited = [False for i in range(n)]
parent = [-1 for i in range(n)]
flag = False
for i in range(n):
    #print(i, flush = True)
    if visited[i] == False:
        if DFS(i, adj, visited, -1, parent) == True:
            ans = []
            #print(parent)
            #print(start, stop)
            ans.append(start)
            while stop != start:
                ans.append(stop)
                stop = parent[stop]
            ans.append(stop)
            ans.reverse()
            for i in range(len(ans)):
                ans[i] += 1
            print(len(ans))
            print(*ans)
            flag = True
            break
if flag == False:
    print('IMPOSSIBLE')