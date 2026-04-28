import sys

input = sys.stdin.readline


def main():
    n, m, q = list(map(int, input().split()))
    dist = [10**15] * (n * n)
    for i in range(n):
        dist[i * n + i] = 0
    for _ in range(m):
        u, v, w = map(lambda x: int(x) - 1, input().split())
        dist[u * n + v] = min(dist[u * n + v], w + 1)
        dist[v * n + u] = min(dist[v * n + u], w + 1)

    for k in range(n):
        for i in range(n):
            for j in range(i + 1, n):
                if dist[i * n + k] + dist[k * n + j] < dist[i * n + j]:
                    dist[i * n + j] = dist[j * n + i] = (
                        dist[i * n + k] + dist[k * n + j]
                    )

    out = []
    for _ in range(q):
        i, j = map(lambda x: int(x) - 1, input().split())
        distance = dist[i * n + j]
        out.append(distance if distance != 10**15 else -1)
    print("\n".join(map(str, out)))


main()