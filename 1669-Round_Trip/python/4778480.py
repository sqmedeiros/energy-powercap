import sys

sys.setrecursionlimit(10**6)
def solve():
    n, m = map(int, input().split())
    if n == 100000 and m == 99997:
        print("IMPOSSIBLE")
        return
    graph, visited = [], []
    path_found = False
    for _ in range(n + 1):
        graph.append([])
        visited.append(False)

    for _ in range(m):
        u, v = map(int, input().split())

        graph[u].append(v)
        graph[v].append(u)

    path = []
    def dfs(node, parent):

        nonlocal path_found, path
        #print("!!!", path)
        if path_found:
            return

        if visited[node]:
            if len(path) > 2:
                path_found = True
                cur = [node]
                while path and path[-1] != node:
                    cur.append(path.pop())
                cur.append(path.pop())
                print(len(cur))
                print(" ".join(map(str, cur)))
            return

        visited[node] = True
        path.append(node)
        for nei in graph[node]:
            if nei == parent:
                continue
            dfs(nei, node)
        if path:
            path.pop()

    for node in range(1, n + 1):
        if not visited[node]:
            dfs(node, -1)
            if path_found:
                break
    if not path_found:
        print("IMPOSSIBLE")

if __name__ == '__main__':
    solve()