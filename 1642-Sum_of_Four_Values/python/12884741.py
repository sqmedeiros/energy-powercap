import sys


def main():
    input = sys.stdin.readline
    n, x = map(int, input().split())
    v = list(map(int, input().split()))

    hm = dict()

    for i in range(n - 1, -1, -1):
        for j in range(i - 1, -1, -1):
            idx = x - v[i] - v[j]
            if idx in hm:
                a, b = hm[idx]
                print(i + 1, j + 1, a + 1, b + 1)
                return

        for j in range(i + 1, n):
            hm[v[i] + v[j]] = (i, j)

    print("IMPOSSIBLE")

main()