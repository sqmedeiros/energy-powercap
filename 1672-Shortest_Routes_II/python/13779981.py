import sys

input_data = sys.stdin.buffer.read().split()
it = iter(input_data)

def nxt():
    return int(next(it))

n = nxt(); m = nxt(); q = nxt()

INF = 10**18
# Matriz de distancias
mat = [[INF] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    mat[i][i] = 0

for _ in range(m):
    a = nxt(); b = nxt(); c = nxt()
    if c < mat[a][b]:  # guardar el menor peso si hay múltiples aristas
        mat[a][b] = mat[b][a] = c

# Floyd-Warshall optimizado
for k in range(1, n + 1):
    mk = mat[k]
    for i in range(1, n + 1):
        mik = mat[i][k]
        if mik == INF:
            continue
        mi = mat[i]
        # recorrido j=1..n
        for j in range(1, n + 1):
            alt = mik + mk[j]
            if alt < mi[j]:
                mi[j] = alt

# Construir salida
out_lines = []
for _ in range(q):
    a = nxt(); b = nxt()
    d = mat[a][b]
    out_lines.append(str(d if d != INF else -1))

sys.stdout.write("\n".join(out_lines))