import sys 
from collections import defaultdict, deque
input = lambda: sys.stdin.readline().strip()

def bfs(start):
  q =deque()
  q.append(start)
  while q:
    front = q.popleft()
    for node in graph[front]:
      if color[node] == 0 :
        q.append(node)
        if color[front] == 1 :
          color[node] = 2
        else:
          color[node] = 1
      elif color[node] == color[front] :
          return False
  return True
graph = {}
n,m = map(int,input().split())
for i in range(m):
    a,b = map(int,input().split())
    if a not in graph :
        graph[a] = [b]
    else:
        graph[a].append(b)
    if b not in graph :
        graph[b] = [a]
    else:
        graph[b].append(a)
color = [0]*(n+1)
ans = []
flag = True
for node in range(1,n+1):
  if color[node] == 0 :
      color[node] = 1
      if node in graph:
          if bfs(node) == False :
            print("IMPOSSIBLE")
            flag = False
            exit()


if flag :
    print(*color[1:])
