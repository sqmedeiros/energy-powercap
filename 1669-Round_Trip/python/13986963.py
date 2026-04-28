import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def roundtrip(n, m, edges):
    from collections import defaultdict

    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visit = [0] * (n + 1)
    parent = [0] * (n + 1)

    for start in range(1, n + 1):
        if visit[start]:
            continue

        stack = [(start, -1)]
        while stack:
            node, par = stack.pop()
            if visit[node]:
                continue
            visit[node] = 1
            parent[node] = par

            for neigh in graph[node]:
                if neigh == par:
                    continue
                if not visit[neigh]:
                    stack.append((neigh, node))
                else:
                    # cycle detected
                    path = [neigh, node]
                    cur = node
                    while parent[cur] != -1 and parent[cur] != neigh:
                        cur = parent[cur]
                        path.append(cur)
                    path.append(neigh)
                    path.reverse()
                    return path
    return "IMPOSSIBLE"

# Input reading
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

result = roundtrip(n, m, edges)
if result == "IMPOSSIBLE":
    print(result)
else:
    print(len(result))
    print(*result)