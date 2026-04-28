import sys

use_local = True
sys.setrecursionlimit(2000000)

n_pupils, m_friends = map(int, sys.stdin.readline().split())

Graph = [[] for _ in range(n_pupils)]
for _ in range(m_friends):
    a, b = map(int, sys.stdin.readline().split())
    Graph[a - 1].append(b - 1)
    Graph[b - 1].append(a - 1)

Visited = [False] * n_pupils
Team = [-1] * n_pupils


def dfs(x, Graph, Visited, Team):
    if Visited[x]:
        return +1
    Visited[x] = True
    for x_new in Graph[x]:
        if Team[x] == Team[x_new]:
            return -1  # impossible
        if Visited[x_new]:
            continue

        Team[x_new] = abs(1 - Team[x])
        code_exit = dfs(x_new, Graph, Visited, Team)
        if code_exit < 0:
            return code_exit
    return +1


for pupil in range(n_pupils):
    if Visited[pupil]:
        continue
    Team[pupil] = 0
    code_exit = dfs(pupil, Graph, Visited, Team)
    if code_exit < 0:
        break

if code_exit < 0:
    print("IMPOSSIBLE")
else:
    for t in Team:
        print(t + 1, end=" ")