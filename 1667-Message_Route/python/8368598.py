from collections import deque
def bfs(graph, parent, n):
    queue = deque()
    queue.append(1)
    visited = [False for i in range(n+1)]
    visited[1] =True
    while len(queue)> 0:
        node = queue.popleft()
        for v in graph[node]:
            if not visited[v]:
                parent[v] = node
                visited[v] =True
                if v == n:
                    return True
                else:
                    queue.append(v)
    return False

def main():
    n,m = map(int, input().split())
    graph = [[] for i in range(n+1)]

    for _ in range(m):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)

    parent = [-1 for _ in range(n+1)]

    found = bfs(graph, parent, n)
    if found:
        path = []
        node = n
        while node != -1:
            path.append(node)
            node = parent[node]
        print(len(path))
        print(*path[::-1])
    else:
        print ("IMPOSSIBLE")




if __name__ == "__main__":
    main()