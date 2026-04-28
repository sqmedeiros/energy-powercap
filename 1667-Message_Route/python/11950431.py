from collections import deque

n_m = list(map(int,input().split()))
n = n_m[0]
m = n_m[1]

m_connections = [list(map(int, input().split())) for i in range(m)]

adj = [[] for i in range(n)]
dist = [-1 for i in range(n)]
origin = [-1 for i in range(n)]
nodes_left = {i for i in range(n)}

for route in m_connections:
    u = route[0]-1
    v = route[1]-1
    adj[u].append(v)
    adj[v].append(u)


Q = deque()
Q.append(0)
nodes_left.remove(0)
dist[0] = 0

while len(Q):
    #print("#adj:", adj)
    #print("#Q:",Q)
    node = Q.popleft()
    routes = adj[node]
    cur_dis = dist[node]
    #print("node:", node)
    #print("routes:", routes)
    #print("nodes left:", nodes_left)

    if node == n:
        break

    for route in routes:
        if route in nodes_left:
            Q.append(route)
            nodes_left.remove(route)
            origin[route] = node
            dist[route] = cur_dis+1


if len(Q) == 0 and len(nodes_left)>0:
    print("IMPOSSIBLE")
    exit()

else:
    prev = n-1
    route_list = []
    while prev != 0:
        route_list.append(prev+1)
        prev = origin[prev]
    route_list.append(prev+1)
    route_list = reversed(route_list)

    print(dist[n-1]+1)
    print(*route_list)
