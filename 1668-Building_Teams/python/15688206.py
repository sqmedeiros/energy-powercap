from collections import defaultdict, deque


def bfs(src):
    if team[src] != 0:
        return True
    queue = deque()
    queue.append(src)
    team[src] = 1
    while queue:
        curr = queue.popleft()
        for neigh in friendship[curr]:
            # print(neigh, team[neigh])
            if team[neigh] == team[curr]:
                return False
            if team[neigh] != 0:
                continue
            team[neigh] = 3 - team[curr]
            queue.append(neigh)

    return True


n, m = [int(i) for i in input().split(" ")]
friendship = defaultdict(list)

for i in range(m):
    u, v = [int(i) for i in input().split(" ")]
    friendship[u].append(v)
    friendship[v].append(u)

team = [0 for i in range(n + 1)]
possible = True
for i in range(1, n + 1):
    if bfs(i) == False:
        possible = False
        break
if possible:
    print(*team[1:])

else:
    print("IMPOSSIBLE")