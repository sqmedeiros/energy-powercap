from sys import maxsize, stdin

n, m, q, *data = [int(x) for x in stdin.read().split()]
row_size = n
dist = [maxsize] * (row_size ** 2)
graph, queries = data[:3 * m], data[3 * m:]
for a, b, length in zip(graph[::3], graph[1::3], graph[2::3]):
    a, b = a - 1, b - 1
    ab = a * row_size + b
    dist[ab] = dist[b * row_size + a] = min(length, dist[ab])
for k in range(row_size):
    row_k = k * row_size
    for i in range(n):
        row_i = i * row_size
        dist_ik = dist[row_i + k]
        if dist_ik == maxsize:
            continue
        for j in range(i):
            ij = row_i + j
            new_dist = dist_ik + dist[row_k + j]
            if new_dist < dist[ij]:
                dist[ij] = dist[j * row_size + i] = new_dist
output = []
for a, b in zip(queries[::2], queries[1::2]):
    a, b = a - 1, b - 1
    res = dist[a * row_size + b] if a != b else 0
    output.append(res if res != maxsize else -1)
print('\n'.join(map(str, output)))