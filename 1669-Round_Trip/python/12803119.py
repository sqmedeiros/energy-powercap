# B – Round Trip
import sys
def solve_B():
    sys.setrecursionlimit(10**7)
    input=sys.stdin.readline
    n,m=map(int,input().split())
    g=[[] for _ in range(n+1)]
    for _ in range(m):
        u,v=map(int,input().split())
        g[u].append(v)
        g[v].append(u)
    visited=[False]*(n+1)
    parent=[0]*(n+1)
    for i in range(1,n+1):
        if not visited[i]:
            stack=[(i,0)]
            while stack:
                v,p=stack.pop()
                if visited[v]:
                    continue
                visited[v]=True
                parent[v]=p
                for u in g[v]:
                    if u==p:
                        continue
                    if visited[u]:
                        path=[v]
                        cur=v
                        while cur!=u:
                            cur=parent[cur]
                            path.append(cur)
                        path.append(v)
                        print(len(path))
                        print(*path[::-1])
                        return
                    stack.append((u,v))
    print("IMPOSSIBLE")

if __name__=="__main__":
    solve_B()