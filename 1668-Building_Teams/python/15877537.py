from collections import deque
import sys

def solve():
    input = sys.stdin.readline

    n, m = map(int, input().split())

    adj = [[] for _ in range(n + 1)]

    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)

    # 0 = unvisited, 1 = team 1, -1 = team 2
    color = [0] * (n + 1)

    for i in range(1, n + 1):
        if color[i] == 0:
            queue = deque([i])
            color[i] = 1

            while queue:
                node = queue.popleft()
                for nei in adj[node]:
                    if color[nei] == 0:
                        color[nei] = -color[node]
                        queue.append(nei)
                    elif color[nei] == color[node]:
                        print("IMPOSSIBLE")
                        return

    # Output result
    print(" ".join("1" if color[i] == 1 else "2" for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()