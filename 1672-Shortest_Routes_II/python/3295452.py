from sys import stdin, stdout

n, m, k = stdin.readline().split()

n = int(n)
m = int(m)
k = int(k)

G = [10**12] * 300000

## матрицу --> в вектор



for i in range(1, n+1):
    G[i * 500 + i] = 0

for i in range(m):
    a,b,c = stdin.readline().split()
    a = int(a)
    b = int(b)
    c = int(c)
    G[a + b * 500] = min(G[a + b * 500], c)
    G[a * 500 + b] = min(G[a * 500 + b], c)

'''
for q in G:
    print(q)
'''

# Флойд  

for u in range(1, n+1):

    for i in range(1, n+1):

        for j in range(1, n+1):

            if (G[i * 500 + u] + G[u * 500 + j]) < G[i * 500 + j]:
                G[i * 500 + j] = G[i * 500 + u] + G[u * 500 + j]
                G[j * 500 + i] = G[i * 500 + u] + G[u * 500 + j]


'''   
for q in G:
    print(*q)
'''

for i in range(k):
    a,b = stdin.readline().split()
    a = int(a)
    b = int(b)
    d = G[a * 500 + b]
    if d == 10**12:
        stdout.write(str(-1) + '\n')
    else:
        stdout.write(str(d) + '\n')
