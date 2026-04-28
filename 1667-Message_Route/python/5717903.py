from collections import deque
N,M = map(int, input().split())

arr = [[] for _ in range(N + 1)]
for _ in range(M):
 x,y = map(int, input().split())
 arr[x].append(y)
 arr[y].append(x)
length, parent = [float("inf") for _ in range(N + 1)],[0 for _ in range(N + 1)]

queue = deque()

length[1],parent[1] = 0,0
queue.append(1)
while queue:
 curr = queue.popleft()
 for adj in arr[curr]:
  if length[adj] == float("inf"):
   length[adj] = length[curr] + 1
   parent[adj] = curr
   queue.append(adj)
if length[-1] == float("inf"):
 print("IMPOSSIBLE")
else:
 print(length[-1] + 1)
 curr = len(arr) - 1
 path = []
 while curr != 0:
  path.append(curr)
  curr = parent[curr]
 path.reverse()
 for i in path:
  print(i, end = " ")