from functools import *
from itertools import *
from collections import *
from math import *
from bisect import *
from heapq import *
from types import *

def bootstrap(f):
    stack = []

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

n, m = map(int, input().split())
g = defaultdict(list)

for i in range(m):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)


path = []
seen = set()
vis = set()

@bootstrap
def dfs(v, p):
    # print(v, p, path)
    vis.add(v)
    if v in seen:
        path.append(v)
        yield True
    seen.add(v)
    path.append(v)
    for i in g[v]:
        if i==p:continue
        res = yield dfs(i, v)
        if res:
            yield True
    path.pop()
    seen.discard(v)
    yield False


for i in range(1, n+1):
    if i not in vis:
        dfs(i,-1)
        if path:
            # print("wow")
            break

# print(path)
if path:
    # print(path)
    res = [path[-1]]
    v = 0
    for i in range(len(path)-2, -1, -1):
        res.append(path[i])
        if res[0]==res[-1]:
            v = 1
            break
    print(len(res))
    print(*res)
else:
    print("IMPOSSIBLE")


