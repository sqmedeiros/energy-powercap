from collections import deque
def Routing():
    comps, cons = map(int, input().split())

    adj = [[] for i in range(comps)]

    for _ in range(cons):
        u,v = map(int, input().split())
        u -= 1 ; v -= 1
        adj[u].append(v)
        adj[v].append(u)

    dist = [-1]*(cons+1) 
    Back = [-1]*(cons+1)
    Goal = comps-1
    A = 0

    Q = deque()
    Q.append(A)
    dist[A] = 0

    while len(Q):
        u = Q.popleft()

        for v in adj[u]:
            if dist[v] == -1:
                Q.append(v)
                dist[v] = 1 + dist[u]
                Back[v] = u
    if dist[Goal] == -1:
        print("IMPOSSIBLE")
        exit()
    else:
        print(dist[Goal]+1)
    Path = []

    t = Goal

    while t != 0:
        Path.append(t)
        t = Back[t]
    Path.append(A)

    Path = reversed(Path)
    for v in Path:
        print(v+1,end=" ")

Routing()