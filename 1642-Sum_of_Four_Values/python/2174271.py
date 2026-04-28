from sys import stdin
input = stdin.readline

def solve():
    n, k = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]

    h = {}
    for i in range(n-1):
        for j in range(i+1, n):
            h[a[i] + a[j]] = (i, j)

    for i in range(n-1):
        for j in range(i+1, n):
            if k - (a[i] + a[j]) in h:
                i2, j2 = h[k - (a[i] + a[j])]
                if i != i2 and j != i2 and i != j2 and j != j2:
                    print(i+1, j+1, i2+1, j2+1)
                    return
    print("IMPOSSIBLE")
solve()