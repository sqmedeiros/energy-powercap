import sys
from collections import deque

def main():
    read = sys.stdin.readline
    n, m = map(int, read().split())
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, read().split())
        adj[a].append(b)
        adj[b].append(a)

    vis = [False] * (n + 1)
    reps = []

    for u in range(1, n + 1):
        if not vis[u]:
            reps.append(u)
            # BFS para marcar la componente
            q = deque([u])
            vis[u] = True
            while q:
                v = q.popleft()
                for w in adj[v]:
                    if not vis[w]:
                        vis[w] = True
                        q.append(w)

    c = len(reps)
    # Imprimimos c-1 nuevas carreteras
    print(c - 1)
    for i in range(c - 1):
        print(reps[i], reps[i + 1])

if __name__ == "__main__":
    main()