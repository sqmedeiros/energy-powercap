import sys
from collections import defaultdict
input = sys.stdin.readline

def bfs(at, g, teams):
  q = []
  q.append(at)
  teams[at] = 1

  while q:
    node = q.pop(0)
    for nei in g[node]:
      if teams[nei] == 0:
        teams[nei] = 3 - teams[node]
        q.append(nei)
      elif teams[nei] == teams[node]:
        return False
  return True





def main():


    n, m = map(int, input().split())
    g = defaultdict(list)

    for _ in range(m):
      a, b = map(int, input().split())
      g[a].append(b)
      g[b].append(a)


    teams = [0 for _ in range(n + 1)]

    possible = True
    for i in range(1, n + 1):
      if teams[i] == 0:
        if not bfs(i, g, teams):
          possible = False
          break

    if not possible:
      print("IMPOSSIBLE")
    else:
      print(" ".join(map(str, teams[1:])))




main()  
