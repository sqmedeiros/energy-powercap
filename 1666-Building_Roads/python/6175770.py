import sys
import heapq
sys.setrecursionlimit(1000000)

def dfs(adj, visited, x):
    visited[x] = True
    for y in adj[x]:
        if not visited[y]:
            dfs(adj, visited, y)

def main():
    n, m = map(int, input().split())
    adj = [[] for _ in range(n+1)]
    for i in range(m):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)

    visited = [False] * (n+1)
    ans = 0
    guys = []
    for i in range(1, n+1):
        if not visited[i]:
            dfs(adj, visited, i)
            guys.append(i)
    print(len(guys)-1)
    anss = []
    for i in range(0, len(guys)-1):
        anss.append(f"{guys[i]} {guys[i+1]}")
    print('\n'.join(anss))



main()