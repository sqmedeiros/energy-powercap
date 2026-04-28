X, Y = input(), input()
N, M = len(X), len(Y)

distance = [[0] * (M+1) for _ in range(N+1)]

for b in range(M+1):
    distance[0][b] = b

for a in range(N+1):
   distance[a][0] = a

for a in range(1, N+1):
    for b in range(1, M+1):
        c1 = distance[a][b-1] + 1
        c2 = distance[a-1][b] + 1
        c3 = distance[a-1][b-1] + (0 if X[a-1] == Y[b-1] else 1)
        distance[a][b] = min(c1, c2, c3)

def edit(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        c1 = edit(a, b-1) + 1
        c2 = edit(a-1, b) + 1
        c3 = edit(a-1, b-1) + (0 if X[a-1] == Y[b-1] else 1)
        return min(c1, c2, c3)

print(distance[N][M])