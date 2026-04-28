from sys import stdin, stdout

s = stdin.readline().split()
dinh, canh = list(map(int, s))
grap = {i: [] for i in range(1, dinh+1)}
visited = [False] * (dinh + 1)

for _ in range(canh):
    s = stdin.readline().split()
    a, b = list(map(int, s))
    grap[a].append(b)
    grap[b].append(a)


def bfs(s):
    q = [s]

    while q:
        u = q[-1]
        visited[u] = True

        for v in grap[u]:
            if not visited[v]:
                q.append(v)
                break
            if v == grap[u][-1]:
                q.pop()


res = []
for j in range(1, dinh+1):
    if not visited[j]:
        res.append(j)
        if not grap[j]:
            continue
        bfs(j)

stdout.write(f'{len(res) - 1}\n')
for i in range(len(res) - 1):
    stdout.write(f'{res[i]} {res[i+1]}\n')