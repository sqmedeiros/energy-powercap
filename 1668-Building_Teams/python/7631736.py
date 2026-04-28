import sys
from collections import defaultdict
import sys

sys.setrecursionlimit(200001) 
#COMPLEXITATE O(n+m)
def is_bipartite(graph, n):
    culoare = [-1] * (n + 1) #asignam culoare -1 pentru pentru toate nodurile
    #functie dfs care atribuie culoriile 1 sau 2 nodurilor

    def dfs(node, c):
        culoare[node] = c 
        for vecin in graph[node]: 
            if culoare[vecin] == -1: #daca un vecin este nevizitat apelam dfs pt el cu 2
                if  dfs(vecin, 3 - c):
                    continue
                else:
                    return False
            elif culoare[vecin] == c:
                return False
        return True

    for i in range(1, n + 1):
        if culoare[i] == -1:
            if  dfs(i, 1):
                continue
            else:
                return "IMPOSSIBLE"

    return culoare[1:]

n, m = map(int, input().split())
graph = defaultdict(list)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

teams = is_bipartite(graph, n)

if teams == "IMPOSSIBLE":
    print("IMPOSSIBLE")
else:
    print(" ".join(map(str, teams)))
