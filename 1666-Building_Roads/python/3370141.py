def main():
    from sys import stdin
    from sys import setrecursionlimit
    setrecursionlimit(1000000)
    n,m = [int(i) for i in input().split(' ')]
    adj = [[] for _ in range(n+1)]
    vis = [0]*(n+1)
    rep = []

    for line in stdin.readlines():
        a,b = map(int,line.strip('\n').split(' '))
        adj[a].append(b)
        adj[b].append(a)
    #print(adj)

    def dfs(adj,vis,x,p):
        if vis[x]:
            return
        vis[x] = p
        for i in adj[x]:
            dfs(adj,vis,i,p)


    for i in range(1,n+1):
        if vis[i] == False:
            rep.append(i)
            dfs(adj,vis,i,i)
    print(len(rep)-1)
    for i in range(len(rep)-1):
        print( f"{rep[i]} {rep[i+1]} ")

main()