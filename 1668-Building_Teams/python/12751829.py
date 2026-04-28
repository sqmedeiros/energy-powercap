import sys
sys.setrecursionlimit(10**6)
from collections import defaultdict
from collections import deque

n, m = map(int, input().split())
graph = defaultdict(list)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

colored = {}

def bipartite_dfs(i, color):
    colored[i] = color
    for child in graph[i]:
        if child not in colored:
            if not bipartite(child, 3 - color):  # Flip between 1 and 2
                return False
        elif colored[child] == color:
            return False
    return True
def bipartite_bfs(i,color):
    q = deque()
    q.append([i,color])
    colored[i] = color
    while(q):
        pop = q.popleft()
        for child in graph[pop[0]]:
            if child not in colored:
                q.append([child,3-pop[1]])
                colored[child]=3-pop[1]
            else:
                if(colored[child]==pop[1]):
                    return False
    # if(is_bipartite):
    #     # for i in range(1,n+1):
    #     #     print(colored[i],end=' ')
    #     return True
    # else:
    #     print('IMPOSSIBLE')
    return True



is_bipartite = True
for i in range(1, n + 1):
    if i not in colored:
        if not bipartite_bfs(i, 1):
            is_bipartite = False
            break

if not is_bipartite:
    print("IMPOSSIBLE")
else:
    for i in range(1, n + 1):
        print(colored[i], end=' ')