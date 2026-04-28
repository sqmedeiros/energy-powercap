n, m = map(int, input().split())
G = [[] for i in range(n + 1)]
que = []
used = [0 for i in range(n + 1)]
p = [[] for i in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

que.append(1)
used[1] = 1
p[1] = -1
b = 0

while b < len(que):
    top = que[b]
    for to in G[top]:
        if not(used[to]):
            que.append(to)
            used[to] = used[top] + 1
            p[to] = top
    b += 1

way = []
if used[n] == 0:
    print('IMPOSSIBLE')
else:
    print(used[n])
    while n != -1:
        way.append(n)
        n = p[n]
    way.reverse()
    for i in way:
        print(i, end = ' ')






