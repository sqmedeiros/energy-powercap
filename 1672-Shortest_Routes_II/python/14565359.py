import sys


readline = sys.stdin.readline

def solve():
    INF = 10**18
    n, m, q = map(int, readline().split())
    graf = [[INF] * n for _ in range(n)]
    for i in range(n):
        graf[i][i] = 0
    for _ in range(m):
        u, v, w = map(int, readline().split())
        u -= 1; v -= 1
        if w < graf[u][v]:
            graf[u][v] = w
            graf[v][u] = w

    for k in range(n):
        frozen = graf[k][:]
        for i in range(n):
            a = frozen[i]
            # if a == INF:
            #     continue
            row_i = graf[i]
            for j in range(i+1, n):
                b = frozen[j]
                # if b == INF:
                #     continue
                total = a + b
                if total < row_i[j]:
                    row_i[j] = total
                    graf[j][i] = total

    res = []
    for _ in range(q):
        u, v = map(int, readline().split())
        d = graf[u-1][v-1]
        res.append(str(d if d != INF else -1))
    sys.stdout.write("\n".join(res))

solve()