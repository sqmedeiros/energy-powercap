import math, sys;input = sys.stdin.readline; S=lambda: input().strip(); I = lambda: int(S()); M= lambda: map(int,S().split()); L = lambda: list(M());mod1=1000000007;mod2=998244353
from collections import defaultdict

sys.setrecursionlimit(9**9)

def dfs(u,visited,adj,p):
    visited[u] = True

    for v in adj[u]:
        if v==p:
            continue

        path.append(v)
        if visited[v]:
            return False

        if not dfs(v,visited,adj,u):
            return False

        path.pop()

        # if visited[v]==u:
        #     return  v
        # elif visited[v]==v:
        #     return dfs(v,visited,adj,u)


    return True




if __name__=="__main__":
    n,m = M()

    adj = defaultdict(list)
    for i in range(m):
        a,b = M()
        adj[a].append(b)
        adj[b].append(a)


    path = [] 
    visited = [False]*(n+1)
    fl= 0
    for i in range(1,n+1):
        if visited[i]==False:
            path.append(i)
            if not dfs(i,visited,adj,0):
                break

            path.pop()

    # print(len(path))
    # print(*path)
    if len(path)==0:
        print("IMPOSSIBLE")
        exit()

    index = path.index(path[-1])
    path = path[index:]

    print(len(path))
    print(*path)

            # if ans!=-1:
            #     fl=1
            #     print(ans,end=" ")
            #     curr = ans

            #     curr = visited[ans]
            #     print(curr,end=" ")
            #     while curr!=ans:
            #         curr = visited[curr]
            #         print(curr,end=" ")
            #     print()
            #     break

    # if fl==0:
    #     print("IMPOSSIBLE")