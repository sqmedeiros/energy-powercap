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


input=sys.stdin.readline
sys.setrecursionlimit(10000)
n,m=map(int,input().split())
sys.setrecursionlimit(10**6)
adj=[[] for i in range(n+1)]
visited=[0]*(n+1)
for i in range(m):
    s,e=map(int,input().split())
    adj[s].append(e)
    adj[e].append(s)




flag=3
@bootstrap
def dfs(node,old,old2):
    global flag
    if flag == 3:
        if visited[node] != 0 and node != old2:
            flag=(node,old)
        if visited[node]==0:
            visited[node]=old
            for i in adj[node]:
                yield dfs(i,node,old)
    yield 

for i in range(1,n+1):
    if flag != 3:
        break
    if visited[i]==0:
        dfs(i,i,-1)
if flag == 3:
    print("IMPOSSIBLE")
else:
    s=flag[0]
    e=flag[1]
    result=[]
    while e != s:
        result.append(e)
        e=visited[e]
    print(len(result)+2)
    print(s,*reversed(result),s)