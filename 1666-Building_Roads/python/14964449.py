import sys
sys.setrecursionlimit(10**7)
from collections import deque, defaultdict

def main():
    data = list(sys.stdin.buffer.read().split())
    it = iter(data)
    n, m = int(next(it)), int(next(it))
    graph = defaultdict(list)

    for _ in range(m):
        u, v = int(next(it)), int(next(it))
        u -= 1
        v -= 1
        graph[u].append(v)
        graph[v].append(u)

    ans = []
    visited = [False]*n

    for i in range(n):
        if visited[i]:
            continue
        visited[i] = True
        ans.append(i)
        Q = deque([i])

        while Q:
            node = Q.popleft()
            for u in graph[node]:
                if visited[u]:
                    continue
                visited[u] = True
                Q.append(u)

    print(len(ans)-1)
    for i in range(1, len(ans)):
        print(1, ans[i]+1)

    return


if __name__ == "__main__":
    main()
