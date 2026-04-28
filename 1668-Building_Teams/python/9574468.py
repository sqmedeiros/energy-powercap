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


n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

group = [0] * (n + 1)


@bootstrap
def dfs(i):
    ans = True
    for ch in graph[i]:
        if group[ch] == 0:
            group[ch] = 3 - group[i]
            d = yield dfs(ch)
            if not d:
                ans = False
                break
        elif group[ch] == group[i]:
            ans = False
            break
    yield ans


for i in range(1, n + 1):
    if group[i] == 0:
        group[i] = 1
        if not dfs(i):
            print("IMPOSSIBLE")
            break
else:
    print(*group[1:])