from queue import Queue as queue
n,m=map(int,input().split())
graph={}
for x in range(n):
    graph[x]=[]
for x in range(m):
    e_start,e_end=map(int,input().split())
    graph[e_start-1].append(e_end-1)
    graph[e_end-1].append(e_start-1)
travel_to_before=[False]*n
main_elem_connect_component=[]
for x in range(n):
    if not travel_to_before[x]:
        bfs_queue=queue()
        bfs_queue.put(x)
        while not bfs_queue.empty():
            next_vertex_explore=bfs_queue.get()
            for y in graph[next_vertex_explore]:
                if not travel_to_before[y]:
                    bfs_queue.put(y)
                    travel_to_before[y] =True
        main_elem_connect_component.append(x)
print(len(main_elem_connect_component)-1)
for x in range(len(main_elem_connect_component)-1):
    print(main_elem_connect_component[x]+1,main_elem_connect_component[x+1]+1)