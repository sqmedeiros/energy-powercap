n,m=map(int,input().split())
g=dict()
for i in range(n):
    g[i+1]=[]
for i in range(m):
    s,d=map(int,input().split())
    g[s].append(d)
    g[d].append(s)
vis=[0]*(n+1)
comp=[]
for i in range(1,n+1):
    if vis[i]==0:
        vis[i]=1
        comp.append([i])
        s=[i]
        while len(s)!=0:
            x=s[-1]
            for j in g[x]:
                if vis[j]==0:
                    comp[-1].append(j)
                    vis[j]=1
                    s.append(j)
                    break
            else:
                s.pop()
print(len(comp)-1)
for i in range(len(comp)-1):
    print(comp[i][0],comp[i+1][0])