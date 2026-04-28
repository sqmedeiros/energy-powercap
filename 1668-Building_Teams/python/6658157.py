from collections import defaultdict, deque


def main():
    def bfs(src: int):
        queue = deque([src])
        colors[src] = 0  # color the start node as n
        while queue:
            front = queue.popleft()
            for neighbor in edges[front]:
                if colors[neighbor] == -1:
                    colors[neighbor] = colors[front] ^ 1
                    queue.append(neighbor)
                else:
                    if colors[neighbor] == colors[front]:
                        return False

        return True

    # I/O
    num_nodes, num_edges = map(int, input().split())
    edges = defaultdict(list)
    for _ in range(num_edges):
        u, v = map(int, input().split())
        edges[u].append(v)
        edges[v].append(u)

    # BFS
    colors = [-1] * (num_nodes + 1)
    IMPOSSIBLE = False
    for i in range(num_nodes):
        if colors[i + 1] == -1:
            if not bfs(i + 1):
                IMPOSSIBLE = True
                break

    if IMPOSSIBLE:
        print("IMPOSSIBLE")
    else:
        print(" ".join([str(v + 1) for v in colors[1:]]))


main()