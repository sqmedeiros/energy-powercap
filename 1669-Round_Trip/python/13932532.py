import sys
sys.setrecursionlimit(10**6)

num_list = list(map(int, input().split()))
cities, num_roads = num_list[0], num_list[1]
adj_list = {i: [] for i in range(1, cities+1)}
for _ in range(num_roads):
    l = list(map(int, input().split()))
    adj_list[l[0]].append(l[1])
    adj_list[l[1]].append(l[0])
visited, stack, stack_set = set(), [], set()
route = []
def dfs(start, parent):
    if route:
        return 
    if start in stack_set:
        i = 1
        route.append(start)
        while stack[-i] != start:
            route.append(stack[-i])
            i += 1
        route.append(start)
        return
    visited.add(start)
    stack.append(start)
    stack_set.add(start)
    for neighbor in adj_list[start]:
        if neighbor != parent:
            dfs(neighbor, start)
    stack.pop()
    stack_set.remove(start)
    return
found = False
for node in adj_list:
    if node not in visited:
        dfs(node, -1)
        if route:
            print(len(route))
            print(" ".join(map(str, route)))
            found = True
            break
if not found:
    print("IMPOSSIBLE")








