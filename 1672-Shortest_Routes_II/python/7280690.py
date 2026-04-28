import sys
input = sys.stdin.readline
inp = sys.stdin.readline
def input(): return inp().strip()


def main():
    n, m, q = map(int, input().split())

    matrix = [[0 if i == j else 10**14 for i in range(n + 1)]
              for j in range(n + 1)]
    for _ in range(m):
        u, v, d = map(int, input().split())
        matrix[v][u] = min(d, matrix[v][u])
        matrix[u][v] = min(d, matrix[v][u])

    for k, dk in enumerate(matrix):
        for i, di in enumerate(matrix):
            for j in range(n + 1):
                if di[k] + dk[j] < di[j]:
                    di[j] = di[k] + dk[j]
    for _ in range(q):
        a, b = map(int, input().split())
        d = matrix[a][b]
        print(-1 if d == 10**14 else d)


if __name__ == "__main__":
    main()