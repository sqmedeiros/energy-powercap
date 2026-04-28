from collections import deque, defaultdict


n, m = map(int, input().split())
adj = defaultdict(list)
colors = [0]*(n+1)


for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

def bfs(s):
    q = deque([s])
    colors[s]=1
    while q:
        node = q.popleft()
        c_color = colors[node]
        new_color = 3 - c_color

        for neigh in adj[node]:
            if colors[neigh]==0:
                colors[neigh]=new_color
                q.append(neigh)
            elif colors[neigh] == c_color:
                return False
    return True

for s in range(1, n+1):
    if colors[s]==0:
        if not bfs(s):
            print("IMPOSSIBLE")
            exit()
print(*colors[1:])








