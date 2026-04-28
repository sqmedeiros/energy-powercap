import sys
def read_1(dtype=int):
    return dtype(input().strip())
def reads_1(dtype=int):
    return list(map(dtype, input().split()))
# def perr(*args, **kwargs): # TODO comment out
#     print(*args, file=sys.stderr, **kwargs)
#
def solve():
    def help(node):
        path = [-1, node]
        vis[node] = 1
        stack = [iter(edges[node])]
        while 1:
            prv = path[-2]
            cur = path[-1]
            nxt = next(stack[-1], None)
            if nxt == prv:
                nxt = next(stack[-1], None)
            if nxt is None:
                stack.pop()
                if len(stack) == 0:
                    return None
                path.pop()
            else:
                path.append(nxt)
                if vis[nxt]:
                    return path[path.index(nxt):]
                vis[nxt] = 1
                stack.append(iter(edges[nxt]))
    n,m = reads_1()
    edges = [[] for ii in range(n)]
    for ii in range(m):
        a,b = reads_1()
        a -= 1
        b -= 1
        edges[a].append(b)
        edges[b].append(a)
    vis = [0] * n
    for node in range(n):
        if vis[node] == 0:
            ans = help(node)
            if ans:
                return ans
#
ans = solve()
if ans is None:
    print('IMPOSSIBLE')
else:
    print(len(ans))
    print(*[ii+1 for ii in ans])