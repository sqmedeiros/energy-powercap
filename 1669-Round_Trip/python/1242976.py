import collections
import heapq
import sys
sys.setrecursionlimit(10**7)
I = lambda : map(int, input().split())
n, m = list(I())
arr = []
for i in range(m):
    arr.append(list(I()))

def getAdjList(arr):
    graph = collections.defaultdict(list)
    for a,b in arr:
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)
    for i in range(n):
        if i not in graph:
            graph[i] = []
    return graph

graph = getAdjList(arr)

ans = []
def dfs(u, pu = -1):
    p[u] = pu
    visited.add(u)
    for v in graph[u]:
        if v == pu:
            continue
        if v in visited:
            #backtrack u to v
            u2 = u
            while u ^v:
                ans.append(u)
                u = p[u]

            ans.append(v)
            ans.append(u2)
            print(len(ans))
            for i in ans:
                print(i+1, end = " ")
            sys.exit(0)

        else:
            dfs(v, u)

visited = set()
p = [-1]*n
for i in range(n):
    if  i not in visited:
        dfs(i)


print("IMPOSSIBLE")
