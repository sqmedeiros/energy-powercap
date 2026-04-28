# n,m = map(int,input().split())
# connections = [[] for _ in range(m)]
# for _ in range(m):
#     a,b = map(int,input().split())
#     connections[a-1].append(b-1)
#     connections[b-1].append(a-1)

# def search(cur,steps,seq):
#     to_visit = connections[cur]
#     count = 0
#     for visiting in to_visit:
#         if visiting == m:
#             return str(steps),seq
#         if visited[visiting - 1]:
#             count += 1
#         if count == len(to_visit):
#             return "IMPOSSIBLE"
#         visited[cur] = True
#         steps += 1
#         seq.append(str(cur + 1) + " ")
#         search(visiting-1,steps,seq)


# cur = 0
# steps = 0
# seq = []
# visited = [False] * n
# steps,seq = search(0,0,[])
# print(steps)
# print(" ".join(seq))

from collections import deque

n, m = map(int, input().split())
adj = [[] for _ in range(n)]
\
for _ in range(m):
    a, b = map(int, input().split())
    adj[a - 1].append(b - 1)
    adj[b - 1].append(a - 1)

visited = [False] * n
parent = [-1] * n

def bfs(start):
    queue = deque([start])
    visited[start] = True
    while queue:
        node = queue.popleft()
        if node == n - 1:
            return True
        for neighbor in adj[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                parent[neighbor] = node
                queue.append(neighbor)
    return False

found = bfs(0)

if not found:
    print("IMPOSSIBLE")
else:
    path = []
    current = n - 1
    while current != -1:
        path.append(current + 1)
        current = parent[current]
    path.reverse()
    print(len(path))
    print(" ".join(map(str, path)))