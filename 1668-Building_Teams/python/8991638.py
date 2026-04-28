from collections import defaultdict, deque

n, m = map(int, input().split())

graph = defaultdict(list)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

teams = {}


def bfs(start):
    nodes_to_visit = deque([start])
    teams[start] = 1
    while nodes_to_visit:
        current = nodes_to_visit.popleft()
        for neighbor in graph[current]:
            if neighbor not in teams:
                teams[neighbor] = 3 - teams[current]
                nodes_to_visit.append(neighbor)
            elif teams[neighbor] == teams[current]:
                return False
    return True


for student in range(1, n + 1):
    if student not in teams:
        if not bfs(student):
            print("IMPOSSIBLE")
            exit()

for i in range(1, n + 1):
    print(teams[i], end=" ")
print()