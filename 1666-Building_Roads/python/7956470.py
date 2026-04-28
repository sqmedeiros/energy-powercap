# import sys
# # sys.stdin = open("CSESBuildingRoads.in")
# input = sys.stdin.readline

n, m = map(int,input().split())
adj = {i: [] for i in range(1, n + 1)}
for i in range(m):
    a, b = map(int,input().split())
    adj[a].append(b)
    adj[b].append(a)
# print(adj)

def dfs(start):
    roads.append(start)
    visited[start] = True
    stack = [start]
    while stack:
        current = stack.pop()
        for neighbor in adj[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                stack.append(neighbor)
    return

visited = [False] * (n + 1)
total_components = 0
roads = []
for i in range(1, n + 1):
    if not visited[i]:
        total_components += 1
        dfs(i)

print(total_components - 1)
for i in range(len(roads) - 1):
    print(roads[i], roads[i + 1])

'''
find the nubmer of connected components and subtract one
store an element from each component and then connect
'''