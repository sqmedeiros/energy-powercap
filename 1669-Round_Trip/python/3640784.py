import sys
sys.setrecursionlimit(200000)

n,m=map(int,input().split())
g=[[] for i in range(n)]
for i in range(m):
    u,v=map(int,input().split())
    g[u-1].append(v-1)
    g[v-1].append(u-1)
# print (g)
def dfs(i,boo,prev):
    # print (i,prev,boo)
    boo[i]=1
    for j in g[i]:
        # print (j)
        if boo[j]==0:
            prev[j]=i
            dfs(j,boo,prev)
        else:
            if j!=prev[i]:
                # print ("here")
                global x
                global y
                x,y=i,j
                # print (x,y,"ghink")
                return (i,j)


x=-1
y=-1
prev=[-2 for i in range(n)]            
boo=[0 for i in range(n)]
for i in range(n):
    if boo[i]==0:
        if prev[i]==-2:
            prev[i]=-1
        ans=dfs(i,boo,prev)
        if ans: break
# print (ans)
# print (x,y)
ans=[x,y]
if ans==[-1,-1]:
    print ("IMPOSSIBLE")
else:
    res=[ans[1]]
    c=ans[1]
    while c!=ans[0]:
        c=prev[res[-1]]
        res.append(prev[res[-1]])
    res.append(res[0])
    print (len(res))
    print (*[x+1 for x in res])    