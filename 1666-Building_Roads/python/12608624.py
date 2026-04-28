from collections import deque

n,m = map(int, input().split())
roads = {}
visited = [False] * (n+1)
for i in range(1,n+1):
    roads[i] = []
groups = []

for _ in range(m):
    a,b = map(int, input().split())
    roads[a].append(b)
    roads[b].append(a)

def bfs(start, acc):
    q = deque()
    q.append(start)

    while len(q) > 0:
        cities = q.popleft()
        for city in roads[cities]:
            if visited[city-1] == False:
                acc.add(city)
                visited[city-1] = True
                q.append(city)

    return acc

for city in range(1, n + 1):
    if visited[city-1] == False:
        cities = (bfs(city, set([city])))
        groups.append(list(cities))

print(len(groups)-1)
for i in range(1,len(groups)):
    print(groups[i-1][0], groups[i][0])



