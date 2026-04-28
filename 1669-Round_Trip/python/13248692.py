# this is a cycle detection and retrieval problem

import sys
sys.setrecursionlimit(10**7)

n,m = map(int,input().split())
adj = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    adj[a].append(b)
    adj[b].append(a)

visited = [False]*(n+1)
parent = [-1]*(n+1)
cycle_start = -1
cycle_end = -1

def solve(node,par):
    global cycle_start, cycle_end
    visited[node] = True

    for next in adj[node]:
        if visited[next] and next == par:
            continue
        if visited[next]:
            cycle_start = next
            cycle_end = node
            return True

        parent[next] = node
        if solve(next,node):
            return True
    return False

found = False

for i in range(1,n+1):
    if not visited[i]:
        if solve(i,-1):
            found  = True
            break

if not found:
    print("IMPOSSIBLE")
else:
    ans = []
    ans.append(cycle_start)
    while cycle_end != cycle_start:
        ans.append(cycle_end)
        cycle_end = parent[cycle_end]
    ans.append(cycle_start)
    ans = ans[::-1]
    print(len(ans))
    print(*ans)


