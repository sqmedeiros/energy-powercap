from sys import stdin, stdout 

n, m = map(int, stdin.readline().split())

prev = [-1]*(n+1)
adj = [[] for _ in range(n+1)]
vis = [False]*(n+1)

for _ in range(m):
    a, b = map(int, stdin.readline().split())
    adj[a].append(b)
    adj[b].append(a)

def dfs(u0):
    q =  [u0]
    while q:
        u = q.pop()
        vis[u] = True
        for v in adj[u]:
            if v == prev[u]: continue
            if vis[v]:
                prev[v] = u
                return v
            else:
                q.append(v)
                prev[v] = u
    return None 

def go():
    for u in range(1, n+1):
        if vis[u]: continue
        vc = dfs(u)
        if vc is not None:
            path = [vc]
            v = prev[vc]
            while v != vc:
                path.append(v)
                v = prev[v]
            path.append(vc)

            stdout.write(str(len(path))+ '\n' )
            for x in path:
                stdout.write(f'{x} ')

            return
    print("IMPOSSIBLE")

go()