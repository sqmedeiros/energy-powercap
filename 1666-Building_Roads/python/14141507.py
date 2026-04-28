import sys
from collections import defaultdict
input = sys.stdin.readline

def bfs(at, vis, g):
  vis[at] = True
  q = []
  q.append(at)

  while q:
    curr = q.pop(0)

    for nei in g[curr]:
      if not vis[nei]:
        vis[nei] = True
        q.append(nei)



def main():


    n, m = map(int, input().split())
    g = defaultdict(list)

    for _ in range(m):
      a, b = map(int, input().split())
      g[a].append(b)
      g[b].append(a)


    vis = [False for _ in range(n + 1)]

    roads = []

    for i in range(1, n + 1):
      if not vis[i]:
        roads.append(i)
        bfs(i, vis, g)

    print(len(roads) - 1)
    for i in range(len(roads) - 1):
      print(roads[i], roads[i + 1])



main()  
