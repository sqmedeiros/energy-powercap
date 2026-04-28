import sys
import threading
input = sys.stdin.readline

############ ---- Input Functions ---- ############
inp = sys.stdin.readline
def input(): return inp().strip()
def ii(): return int(input())
def mi(): return map(int, input().split())
def li(): return list(map(int, input().split()))


def main():
    n, m, q = map(int, input().split())

    matrix = [[0 if i == j else 10**14 for i in range(n + 1)]
              for j in range(n + 1)]
    for _ in range(m):
        u, v, d = map(int, input().split())
        # # if d < matrix[v][u]:/
        #     matrix[v][u] = d
        #     matrix[u][v] = d
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