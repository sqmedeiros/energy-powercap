# Name : Anurag Samota
# Problem : Building Teams
# Roll. No. : M25CSE007



import sys
from collections import deque

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    it = iter(data)
    n = next(it)
    m = next(it)
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        a = next(it); b = next(it)
        adj[a].append(b)
        adj[b].append(a)

    color = [0] * (n + 1)  # 0 = unvisited, 1 or 2 = teams

    for s in range(1, n + 1):
        if color[s] != 0:
            continue
        color[s] = 1
        q = deque([s])
        while q:
            u = q.popleft()
            for v in adj[u]:
                if color[v] == 0:
                    color[v] = 3 - color[u]
                    q.append(v)
                elif color[v] == color[u]:
                    print("IMPOSSIBLE")
                    return

    print(" ".join(map(str, color[1:])))

if __name__ == "__main__":
    main()

