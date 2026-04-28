from collections import deque

n,m = list(map(int,input().split()))

lst_ = []
for _ in range(m):
  lst_.append(list(map(int,input().split())))

lst = [[] for _ in range(n+1)]
for x in lst_:
  lst[x[0]].append(x[1])
  lst[x[1]].append(x[0])

first =1
last = n
dq = deque()
dq.append(first)

visited = [False]*(n+1)
visited[first] = True

dist = [-1] *(n+1)
dist[first] = 0

prev = [-1] * (n+1)

while dq:
  deleted = dq.popleft()
  for x in lst[deleted]:
    if not visited[x]:
      prev[x] = deleted
      dist[x] = dist[deleted] + 1
      dq.append(x)
      visited[x] = True
if prev[last] == -1:
  print("IMPOSSIBLE")
else:
  ans = [last]
  x = last
  while x != first:
    ans.append(prev[x])
    x = prev[x]
  ans.reverse()
  print(dist[last]+1)
  print(*ans)