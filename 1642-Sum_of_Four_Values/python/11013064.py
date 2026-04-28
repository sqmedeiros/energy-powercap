import sys
input = sys.stdin.read
def solve():
    data = input().split()
    n = int(data[0])
    x = int(data[1])
    a = list(map(int, data[2:]))
    hm = {}

    for i in range(n-1):
        for j in range(i + 1, n):
            target = x - a[i] - a[j]
            if target in hm and i!=hm[target][0] and j!=hm[target][1] and j!=hm[target][0] and i!=hm[target][1]:
                print(i + 1, hm[target][0] + 1, hm[target][1]+1, j + 1)
                return
            if not a[i] + a[j] in hm:
                hm[a[i] + a[j]] = (i,j)

    print("IMPOSSIBLE")

solve()
