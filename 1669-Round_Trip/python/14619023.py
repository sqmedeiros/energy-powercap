from collections import deque

n,m = list(map(int, input().split()))

adjList = []
visited = []
parent = []
for i in range(n+1):
    adjList.append([])
    visited.append(0)
    parent.append(-1)

for i in range(m):
    a,b = list(map(int, input().split()))
    adjList[a].append(b)
    adjList[b].append(a) 

for i in range(1,n+1):
    if(not visited[i]):
        stack = deque([(i,-1)])
        visited[i] = 1
        while(stack):
            node,par = stack.pop()
            for nghbr in adjList[node]:
                if(not visited[nghbr]):
                    visited[nghbr] = 1
                    stack.append((nghbr,node))
                    parent[nghbr] = node
                elif(nghbr != par):
                    # Cycle found! nghbr is the ancestor and node is the descendant
                    cycle = []
                    current = node


                    # Backtrack from the current node until the common ancestor (neighbor) is reached
                    while (current != parent[nghbr]):
                        cycle.append(current)
                        current = parent[current]
                    cycle.append(parent[nghbr])
                    cycle.append(nghbr)
                    cycle.append(node)
                    print(len(cycle))
                    for ele in cycle:
                        print(ele, end = " ")
                    exit(0)
print("IMPOSSIBLE")




