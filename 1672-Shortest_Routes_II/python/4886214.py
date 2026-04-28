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

    dist = [[0 if i == j else 10**14 for i in range(n + 1)]
            for j in range(n + 1)]
    for _ in range(m):
        u, v, d = map(int, input().split())
        if d < dist[v][u]:
            dist[v][u] = d
            dist[u][v] = d

    for k, dk in enumerate(dist):
        for i, di in enumerate(dist):
            for j in range(n + 1):
                if di[k] + dk[j] < di[j]:
                    di[j] = di[k] + dk[j]

    for _ in range(q):
        a, b = map(int, input().split())
        d = dist[a][b]
        print(-1 if d == 10**14 else d)


if __name__ == "__main__":
    main()