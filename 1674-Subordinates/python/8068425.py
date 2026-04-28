import sys
sys.setrecursionlimit(200006)  # set recursion limit
def dfs(v) :
    res = 1
    for u in graph[v] :
        if(u == p[v]):
            continue

        res += dfs(u)
    sub[v] = res - 1
    return res


n = int(input())
graph = [[] for _ in range(n)]
sub = [0 for _ in range(n)]
p = [1] + list(map(int, input().split()))
p = [x - 1 for x in p]
for ind, par in enumerate(p):
    graph[ind].append(par)
    graph[par].append(ind)
dfs(0)
print(*sub)
