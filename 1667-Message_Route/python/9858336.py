#-----------------MAIN---------------------
# import math
# import sys
# sys.stdin = open('input.txt','r')
# sys.stdout = open('output.txt','w')


from queue import Queue


def solve():
    # n = int(input())
    # s=input()
    n,m=map(int,input().split())
    # a=list(map(int,input().split()))
    # b=list(map(int,input().split()))

    adj = [[] for _ in range(n+1)]

    for _ in range(m):
        a,b=map(int,input().split())
        adj[a].append(b)
        adj[b].append(a)

    vis=[0]*(n+1)

    q=Queue()
    q.put(1)
    vis[1]=1
    parent={1:-1}

    while not q.empty():
        u = q.get()
        if u==n:
            break

        for v in adj[u]:
            if vis[v]==0:
                q.put(v)
                parent[v]=u
                vis[v]=1

    if vis[n]==0:
        print("IMPOSSIBLE")
        return

    path=[]
    u=n
    while u!=-1:
        path.append(u)
        u = parent[u]

    print(len(path))
    for i in range(len(path)-1,-1,-1):
        print(path[i],end=" ")
    print()






solve()