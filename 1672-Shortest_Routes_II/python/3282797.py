from sys import stdin, stdout
n, m, q = map(int, input().split())

G = [10**12] * 300000


for _ in range(m):
    a, b, c = stdin.readline().split()
    a = int(a)
    b = int(b)
    c = int(c)
    G[a + b * 500] = min(G[a + b * 500], c)
    G[a * 500 + b] = min(G[a * 500 + b], c)


for i in range(1, n+1):
    G[i * 500 + i] = 0


for k in range(1, n+1):
    for i in range(1, n+1):
        dis_ki = G[i * 500 + k]
        if k == i or dis_ki == 10**12:
            continue
        for j in range(1, n+1):
            new_dis = dis_ki + G[k * 500 + j]
            if new_dis < G[i * 500 + j]:
                G[i * 500 + j] = G[j * 500 + i] = new_dis

for _ in range(q):
    a, b = stdin.readline().split()
    a = int(a)
    b = int(b)
    dist = G[a * 500 + b]
    if dist == 10**12:
        stdout.write(str(-1) + '\n')
    else:
        stdout.write(str(dist) + '\n')