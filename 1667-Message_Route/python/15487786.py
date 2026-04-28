#https://cses.fi/problemset/task/1667/
#Gráf algoritmus feladat

n,m=map(int,input().split())
routes=[]
for i in range(m):
    routes.append(list(map(int, input().split())))

from collections import deque





def bfs(n,m,graph):
    parent = {1: 0}
    visited = set([1])
    queue=deque([1])

    while queue:
        current=queue.popleft()

        for neighbour in graph[current]:
            if neighbour not in visited:
                queue.append(neighbour)
                visited.add(neighbour)
                parent[neighbour] = current
    if(n not in parent):
        print("IMPOSSIBLE")
        return()
    route=[]
    current=n
    sum=0
    while current != 0:
        route.append(current)
        current=parent[current]
        sum+=1
    route.reverse()
    temp=" ".join(map(str, route))
    print(sum)
    print(temp)





def createGraph(n,routes):
    graph= {}
    for i in range(1,n+1):
        graph[i] = []
    for route in routes:
        keys= graph.keys()
        if(route[0] in keys):
            graph[route[0]].append(route[1])
            graph[route[1]].append(route[0])
        else:
            graph[route[0]] = [route[1]]
    return graph




graph=createGraph(n,routes)

bfs(n,m,graph)