from collections import defaultdict, deque

def solve(n, m, edges):

    graph = defaultdict(set)
    for u, v in edges: graph[u-1].add(v-1); graph[v-1].add(u-1)

    res = [0]*n

    for i in range(n):
        if res[i] != 0 : continue

        res[i] = 1
        queue = deque([(0, i)])
        while queue:
            grp, curr = queue.popleft()

            for ne in graph[curr]:
                if res[ne] == grp + 1: return ['IMPOSSIBLE']
                if res[ne] != 0: continue
                res[ne] = (grp^1) + 1
                queue.append((grp^1, ne))

    return res

n, m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]
print(*solve(n, m, edges))