from collections import deque

n,m = map(int,input().split())
adj=[[]for i in range(n+1)] 

def bfs(node):
    queue = deque()
    queue.append(node)
    colors[node]=1
    while queue:
        current = queue.popleft()
        currentCol = colors[current]
        nextCol = 3-currentCol
        for nigg in adj[current]:
            if colors[nigg] == 0:
                colors[nigg] = nextCol
                queue.append(nigg)
            elif colors[nigg] == currentCol:
                return False

    return True


for i in range(m):
    a,b=map(int,input().split())
    adj[a].append(b)
    adj[b].append(a)

colors=[0]*(n+1)

for i in range(1,n+1):
    if colors[i] == 0:
        if not bfs(i):
            print('IMPOSSIBLE')
            exit()

print(*colors[1:])

