# message routing
"""
Syrjälä's network has n computers and m connections. Your task is to 
find out if Uolevi can send a message to Maija, and if it is possible, 
what is the minimum number of computers on such a route.
 The first input line has two integers n and m: the number of computers and connections. 
The computers are numbered 1,2,...,n. Uolevi's computer is 1 and Maija's computer is n.
Then, there are m lines describing the connections.
Each line has two integers a and b: there is a connection between those computers.
Every connection is between two different computers, and there is at most one connection between any two computers.
  If it is possible to send a message
first print k: the minimum number of computers on a valid route. 
After this, print an example of such a route. You can print any valid solution.
If there are no routes, print "IMPOSSIBLE".
"""

# input
n,m = map(int, input().split())
adj = [[] for _ in range(n+1)]
for _ in range(m):
    src, dst = map(int, input().split())
    adj[src].append(dst)
    adj[dst].append(src)

from collections import deque
q = deque([1])
visited = [False]*(n+1)
parent = [0]*(n+1)
found = False
visited[1]=True
while q:
    v = q.popleft()
    if v == n :
        found = True
        break
    for nei in adj[v]:
        if not visited[nei]:
            q.append(nei)
            parent[nei]=v
            visited[nei]=True

if not found:
    print("IMPOSSIBLE")
else:
    path = []
    curr = n
    while curr != 0:
        path.append(curr)    
        curr = parent[curr]
    path.reverse()
    print(len(path))
    print(*path)