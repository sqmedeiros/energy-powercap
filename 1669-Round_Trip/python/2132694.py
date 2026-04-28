import sys
from types import GeneratorType
def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to
    return wrappedfunc

n,m=map(int,input().split())
sys.setrecursionlimit(10**6)
adj=[[] for i in range(n+1)]
visited=[-1]*(n+1)
for i in range(m):
    s,e=map(int,input().split())
    adj[s].append(e)
    adj[e].append(s)

kk=[]
@bootstrap
def dfs(node,old,distance):
    if visited[node]== -1 and len(kk) < 1:
        visited[node]=(distance,old)
        for a in adj[node]:
            if visited[a] != -1 and a != old:
                kk.append((a,node))
            yield dfs(a,node,distance+1)
    yield

for i in range(1,n+1):
    if visited[i] == -1 and len(kk) <1:
        dfs(i,-1,0)

if len(kk) == 0:
    print("IMPOSSIBLE")
else:
    result=[]
    a,node=kk[0]
    j=node
    while node != a:
        result.append(node)
        node=visited[node][1]
    print(len(result)+2)
    print(a,*reversed(result),a)