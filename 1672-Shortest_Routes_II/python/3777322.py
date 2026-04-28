from sys import maxsize, stdin

n, m, q, *data = [int(x) for x in stdin.read().split()]
dist = [maxsize] * (n * n)
graph, queries = data[:3 * m], data[3 * m:]
for a, b, length in zip(graph[::3], graph[1::3], graph[2::3]):
    a, b = a - 1, b - 1
    ab = a * n + b
    dist[ab] = dist[b * n + a] = min(length, dist[ab])
for k in range(n):
    row_k = k * n
    for i in range(n):
        row_i = i * n
        dist_ik = dist[row_i + k]
        if dist_ik == maxsize:
            continue
        for j in range(i):
            ij = row_i + j
            new_dist = dist_ik + dist[row_k + j]
            if new_dist < dist[ij]:
                dist[ij] = dist[j * n + i] = new_dist
output = []
for a, b in zip(queries[::2], queries[1::2]):
    a, b = a - 1, b - 1
    res = dist[a * n + b] if a != b else 0
    output.append(res if res != maxsize else -1)
print('\n'.join(map(str, output)))