import sys
input = sys.stdin.readline
inp = sys.stdin.readline
def input(): return inp().strip()

def solve():
    n, m, q = map(int, input().split())
    mat = [[0 if i == j else 10**14 for i in range(n + 1)] for j in range(n + 1)]

    for i in range(m):
        start, end, d = map(int, input().split())
        mat[start-1][end-1] = min(d, mat[start-1][end-1])
        mat[end-1][start-1] = min(d, mat[start-1][end-1])
    for k, dk in enumerate(mat):
        for i, di in enumerate(mat):
            for j in range(n + 1):
                if di[k] + dk[j] < di[j]:
                    di[j] = di[k] + dk[j]
    for i in range(q):
        start, end = map(int, input().split())
        d = mat[start-1][end-1]
        print(-1 if d == 10**14 else d)

if __name__ == "__main__":
    solve()