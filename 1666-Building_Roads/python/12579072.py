#Attempted Optimization for python - using stack DFS instead of recursion
#Group CP_Uncs (Koneshka+Aidan+Oscar)
def dfs(node):
    stack = [node]
    while len(stack) > 0:
        node = stack.pop()
        if not has_been_visited[node]:
            has_been_visited[node] = True
            for connected_road in adjacency_list[node]:
                if not has_been_visited[connected_road]:
                    stack.append(connected_road)

num_cities, num_roads = map(int,input().split())

list_of_roads = []

for _ in range(num_roads):
    list_of_roads.append(list(map(int, input().split())))

adjacency_list = []
for _ in range(num_cities):
    adjacency_list.append([])

has_been_visited = [False] * num_cities

for i in range(len(list_of_roads)):
    adjacency_list[list_of_roads[i][0] - 1].append(list_of_roads[i][1] - 1)
    adjacency_list[list_of_roads[i][1] - 1].append(list_of_roads[i][0] - 1)

new_roads = []
#Run DFS on each of the components, each time there's an unconnected one add it to the list
#This way we always start with the first road 
for i in range(num_cities):
    if not has_been_visited[i]:
        new_roads.append(i)
        #Run dfs to mark all the roads connected to this one
        dfs(i)

#The amount of components to connect are the number of unconnected components minus one
num_new_roads = len(new_roads) - 1
print(num_new_roads)

#Process the routes
for i in range(1, num_new_roads + 1):
    print(new_roads[i - 1] + 1, new_roads[i] + 1)
