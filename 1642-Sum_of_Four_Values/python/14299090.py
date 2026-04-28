import sys
input = lambda: sys.stdin.readline().strip()
n, k = map(int, input().split())
a = list(map(int, input().split()))
arr = [(a[i], i + 1) for i in range(n)]
arr.sort()
d = {}
for i in range(n):
    for j in range(i + 1, n):
        need = k - (arr[i][0] + arr[j][0])
        if need in d:
            x, y = d[need]
            if len({x, y, arr[i][1], arr[j][1]}) == 4:
                print(arr[i][1], arr[j][1], x, y)
                exit()
        s = arr[i][0] + arr[j][0]
        if s not in d:
            d[s] = (arr[i][1], arr[j][1])
print("IMPOSSIBLE")