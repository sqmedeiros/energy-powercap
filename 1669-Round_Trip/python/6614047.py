import sys
input = sys.stdin.readline

n, m = map(int, input().split())
g = [[] for _ in range(n+1)]
for i in range(m):
    a,b = [int(x) for x in input().split()]
    g[a].append(b)
    g[b].append(a)
vis = [ 0 for _ in range(n+1)]

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

@bootstrap
def dfs(u, par, path):
    vis[u] = 1
    path.append(u)
    for v in g[u]:
        if v == par: continue
        if vis[v] and v != par:
            ans = [v]
            while path[-1] != v:
                ans.append(path.pop())
            ans.append(v)
            print(len(ans))
            print(*ans)
            exit()
        yield dfs(v, u, path)
    path.pop()
    yield 

for i in range(1, n+1):
    if not vis[i]: dfs(i, -1, [])
print("IMPOSSIBLE")
