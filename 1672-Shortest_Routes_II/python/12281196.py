import sys

INF = 10**14
input = sys.stdin.buffer.readline  # Redefine input for speed.

n, m, q = map(int, input().split())
distance = [[INF if i != j else 0 for j in range(n+1)] for i in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    distance[a][b] = distance[b][a] = min(distance[a][b], c)

# Run Floyd-Warshall's algorithm to find the shortest paths.
for k, dist_k in enumerate(distance):
    for j, dist_j in enumerate(distance):
        for i in range(1, n+1):
            dist_j[i] = min(dist_j[i], dist_j[k] + dist_k[i])

answers = []
for _ in range(q):
    a, b = map(int, input().split())
    answers.append(-1 if distance[a][b] == INF else distance[a][b])
print('\n'.join(map(str, answers)))