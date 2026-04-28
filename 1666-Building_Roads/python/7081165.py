from collections import defaultdict
import sys

sys.setrecursionlimit(10**5)
def solve(n,adj):
    visited=set()
    start=set()
    def dfs(i):
        if i in visited: return
        visited.add(i)
        for j in adj[i]:
            if j not in visited:
                dfs(j)
    for i in range(1,n+1):
        if i not in visited:
            start.add(i)
            dfs(i)
    print(len(start)-1)
    root=start.pop()
    for i in start:
        print(root,i)




if __name__ == '__main__':
    n,m=map(int,input().split())
    adj=defaultdict(list)
    for _ in range(m):
        u,v=map(int,input().split())
        adj[u].append(v)
        adj[v].append(u)
    solve(n,adj)
