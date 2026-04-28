"""
5 5
1 2
1 3
1 4
2 3
5 4
"""
from collections import deque
n,m = (int(i) for i in input().split())
graph = [[False] for i in range(n+1)]
for road in range(m):
    a,b = (int(i) for i in input().split())
    graph[a].append(b)
    graph[b].append(a)
not_found = False
to_visit = deque()
#push a start vertex to the to_visit deque
to_visit.appendleft(1)
#set this vertex as visited
graph[1][0] = True
while to_visit:
    prev_vertex = to_visit.pop()
    for next_vertex in graph[prev_vertex][1:]:
        if graph[next_vertex][0] != False:
            continue
        graph[next_vertex][0] = prev_vertex
        to_visit.appendleft(next_vertex)
    if prev_vertex == n:
        break
else:
    not_found = True
unroll = graph[n][0]

if not_found:
    print("IMPOSSIBLE")
else:
    output = deque()
    output.appendleft(n)
    while unroll != True:
        output.appendleft(unroll)
        unroll = graph[unroll][0]
    output.appendleft(1)
    print(len(output))
    print(*output)
