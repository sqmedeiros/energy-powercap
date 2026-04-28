import sys
from collections import deque

def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    # 0 = unvisited, 1 = team1, 2 = team2
    team = [0] * (n+1)

    def bfs(start):
        queue = deque([start])
        team[start] = 1
        while queue:
            u = queue.popleft()
            for v in graph[u]:
                if team[v] == 0:
                    team[v] = 3 - team[u]  # alternate team
                    queue.append(v)
                elif team[v] == team[u]:
                    return False
        return True

    for i in range(1, n+1):
        if team[i] == 0:
            if not bfs(i):
                print("IMPOSSIBLE")
                return

    print(' '.join(map(str, team[1:])))

if __name__ == "__main__":
    main()