import sys
sys.setrecursionlimit(10**8)
[n, m] = [int(x) for x in input().split()]
adj = [[] for i in range(n)]

def connected():

  visited = [True for i in range(n)]
  cc = []
  for i in range(n):
    if visited[i]:
      cc.append(dfs(visited, [], i))

  return cc
def dfs(visited, temp, v):
  visited [v] = False
  temp.append(v+1)
  flag = 0
  for i in adj[v] :
    if visited[i]:

      temp = dfs(visited, temp, i)

  return temp

for i in range(m):
  [u, v] = [int(x) for x in input().split()]
  adj[u-1].append(v-1)
  adj[v-1].append(u-1)

s = connected()
print(len(s)-1)
for i in range(1, len(s)):
  print(s[i-1][-1], s[i][-1])