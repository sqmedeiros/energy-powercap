# https://cses.fi/problemset/task/1669
# Idea: DFS
import sys
sys.setrecursionlimit(int(1e6))

amountOfCities, amountOfRoads = map(int, input().split())
adj = [[] for _ in range(amountOfCities)]
visited = [0] * amountOfCities 
back = [-1] * amountOfCities

for i in range(amountOfRoads):
    cityOne, cityTwo = map(int, input().split())

    adj[cityOne - 1].append(cityTwo - 1)
    adj[cityTwo - 1].append(cityOne - 1)

startingVal = -1
endingVal = -1

def DFS(u):
    global startingVal
    global endingVal

    if visited[u]: 
        return 

    visited[u] = 1

    for v in adj[u]:
        if v != u and not visited[v]:
            back[v] = u
            DFS(v)

        elif visited[v] and back[v] != u and back[u] != v:
            startingVal = u
            endingVal = v 

for u in range(amountOfCities):
    if not visited[u]:
        DFS(u)

# Print results
if startingVal == -1:
    print("IMPOSSIBLE")

if startingVal > -1:
    path = []

    path.append(startingVal + 1)
    path.append(endingVal + 1)

    currentPos = back[endingVal]
    while currentPos != startingVal:
        path.append(currentPos + 1)
        currentPos = back[currentPos]
    path.append(currentPos + 1)

    print(len(path))
    print(*path)