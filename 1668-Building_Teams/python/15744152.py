import sys
from collections import deque


def solve():
    # Fast I/O: Read all at once and split by whitespace
    data = sys.stdin.read().split()
    if not data:
        return

    n = int(data[0])
    m = int(data[1])

    # Use list of lists for better speed/memory
    adj = [[] for _ in range(n + 1)]
    pointer = 2
    for _ in range(m):
        u = int(data[pointer])
        v = int(data[pointer + 1])
        adj[u].append(v)
        adj[v].append(u)
        pointer += 2

    colors = [0] * (n + 1)  # 0: uncolored, 1: team 1, 2: team 2

    for i in range(1, n + 1):
        if colors[i] == 0:
            colors[i] = 1
            queue = deque([i])

            while queue:
                curr = queue.popleft()
                current_color = colors[curr]
                next_color = 2 if current_color == 1 else 1

                for neighbor in adj[curr]:
                    if colors[neighbor] == 0:
                        colors[neighbor] = next_color
                        queue.append(neighbor)
                    elif colors[neighbor] == current_color:
                        # If a neighbor already has the SAME color, it's not bipartite
                        print("IMPOSSIBLE")
                        return

    # Print results for nodes 1 to n
    print(*(colors[1:]))


if __name__ == "__main__":
    solve()