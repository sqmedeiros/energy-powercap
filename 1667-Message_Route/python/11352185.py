from collections import deque

class node:
    def __init__(self, key):
        self.key = key
        self.parent = self

temp = input().split()
n = int(temp[0])
m = int(temp[1])

nodes = [node(i) for i in range(0,n+1)]
adj = [[] for i in range(0,n+1)]

for i in range(m):
    temp = input().split()
    adj[int(temp[0])].append(int(temp[1]))
    adj[int(temp[1])].append(int(temp[0]))

# print(adj)

def bfs(s,e):
    queue = deque([s])
    seen = [0 for i in range(0,n+1)]
    seen[s] = 1

    while queue:
        curr = queue.popleft()
        for i in adj[curr]:
            if seen[i] == 0:
                seen[i] = 1
                nodes[i].parent = nodes[curr]
                queue.append(i)
                if i == e:
                    return True
    return False

res = bfs(1,n)
if res:
    back = nodes[n]
    length = 1
    temp = []
    while (back.key != 1):
        temp.append(back.key)
        back = back.parent
        length += 1
    print(length)
    print("1 ", end='')
    for i in reversed(temp):
        print(f"{i} ", end='')
else:
    print("IMPOSSIBLE")