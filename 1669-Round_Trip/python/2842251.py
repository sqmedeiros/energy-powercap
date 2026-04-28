"""
1) Do breadth search storing the position of previous vertex
2) If we found a vertex which has a previous vertex assigned,
we need to add this vertex as our endpoint + previous vertex,
and trace back to the city which already had a position + starting count of elements in a cycle 
3) print vertices in a cycle 
"""
from collections import deque
n,m = (int(i) for i in input().split())
graph = [[False] for i in range(n+1)]
for friendship in range(m):
    a,b = (int(i) for i in input().split())
    graph[a].append(b)
    graph[b].append(a)
unroll = deque()
to_visit = deque()

def bts():
    for start in range(1,n+1):
        counter = 1 
        if graph[start][0] == False:
            graph[start][0] = start
            to_visit.appendleft(start)
            while to_visit:
                node = to_visit.pop()
                for neighbor in graph[node][1:]:
                    if graph[neighbor][0] == False:
                        counter +=1
                        graph[neighbor][0] = node
                        to_visit.appendleft(neighbor)
                    elif counter > 2 and graph[node][0]!=neighbor:
                        counter = 2
                        unroll = deque()
                        unroll.appendleft(node)
                        unroll.append(neighbor)
                        stopnode = node
                        currentnode = neighbor
                        while currentnode != stopnode:
                            if stopnode == graph[currentnode][0]:
                                counter +=1
                                unroll.append(stopnode)
                                break
                            stopnode = graph[stopnode][0]
                            counter +=1
                            unroll.appendleft(stopnode)
                            if currentnode == stopnode:
                                break
                            currentnode = graph[currentnode][0]
                            counter +=1
                            unroll.append(currentnode)

                        print(counter)
                        print(*unroll)
                        return 1 
                    else:
                        pass               


    else:   
        print('IMPOSSIBLE')
        return 0
bts()

"""
5 4
1 2
3 4
5 4
5 3
"""