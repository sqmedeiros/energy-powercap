from collections import defaultdict
import sys

# Not recommended to use this, as it is not a good practice to change the recursion limit
# sys.setrecursionlimit(10**6)

# def dfs(g, v, visited):
#   if v in visited:
#     return
#   visited.add(v)
#   print(v)
#   for i in g[v]:
#     if not visited[i]:
#       dfs(g, i, visited)

# It is better to use a loop instead of recursion
def dfs_iter(g, v, visited):
  stack = [v]
  while stack:
    v = stack.pop()
    if v in visited:
      continue
    visited.add(v)
    stack += g[v]

def main():
  n,m = map(int, input().split())
  d = defaultdict(list)
  for _ in range(m):
    a,b = map(int, input().split())
    d[a].append(b)
    d[b].append(a)
  reps = []

  # 
  v = set(range(1, n+1))
  while v:
    c = set()
    itr = iter(v) # iterator
    p = next(itr)
    reps.append(p)
    dfs_iter(d, p, c) # all nodes reachable from node p
    v -= c
  # print(reps)
  print(len(reps)-1)
  for i in range(len(reps)-1):
    print(reps[i], reps[i+1])


if __name__ == '__main__':
  try:
    sys.stdin = open('input.txt', 'r')
  except FileNotFoundError:
    pass
  main()