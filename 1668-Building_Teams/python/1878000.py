o = lambda:map(int,input().split())
n,m = o()
g = [[] for i in range(n)]
for i in range(m):
    x,y = o()
    x-=1
    y-=1
    g[x]+=[y]
    g[y]+=[x]
c = [0]*n
for i in range(n):
    if c[i]<1:
        c[i] = 1
        q =[i]
        while q:
            s = q.pop()
            for j in g[s]:
                if c[j]<1:
                    c[j] = c[s]%2+1
                    q+=[j]
                if c[j]==c[s]:
                    print("IMPOSSIBLE")
                    exit()
print(*c)
