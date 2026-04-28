import collections
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return

    n = int(data[0])
    m = int(data[1])
    graph = [[] for _ in range(n+1)]

    index = 2
    for _ in range(m):
        a = int(data[index])
        b = int(data[index+1])
        index += 2
        graph[a].append(b)
        graph[b].append(a)

    color = [0] * (n+1)

    for i in range(1, n+1):
        if color[i] != 0:
            continue
        queue = collections.deque([i])
        color[i] = 1

        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if color[neighbor] == 0:
                    color[neighbor] = 3 - color[node]
                    queue.append(neighbor)
                elif color[neighbor] == color[node]:
                    print("IMPOSSIBLE")
                    return

    print(" ".join(str(color[i]) for i in range(1, n+1)))

if __name__ == "__main__":
    main()