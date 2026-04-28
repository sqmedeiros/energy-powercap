global n,m,d,ans
n,m=map(int,input().split())

from collections import defaultdict

def v():
    return set()

d=defaultdict(v)

def dfs(s,c):
    global ans
    vis.add(s)
    ans[s]=c

    st=[s]

    while(st):
        p=st.pop()

        for i in d[p]:
            if(i not in vis):
                st.append(i)
                vis.add(i)
                ans[i]=3-ans[p]
            else:
                if(ans[i]==ans[p]):
                    return False
    return True


for i in range(m):
    x,y=map(int,input().split())
    d[x].add(y)
    d[y].add(x)

vis=set()
g=defaultdict()

ans=[0 for i in range(n+1)]
f=1
for i in range(1,n+1):
    if(i not in vis):
        if(not dfs(i,1)):
            f=0
            break

if(f):
    ans.pop(0)
    print(*ans)
else:
    print('IMPOSSIBLE')