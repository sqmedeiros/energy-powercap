import sys
data = sys.stdin.read().split()
n, x = int(data[0]), int(data[1])
li = list(map(int, data[2: n + 2]))
sum = {}
for i in range(n - 1, -1, -1):
    for j in range(i - 1, -1, -1):
        temp = x - li[i] - li[j]
        if temp in sum:
            k, l = sum[temp]
            print(i + 1, j + 1, k + 1, l + 1)
            exit()
    for j in range(i + 1, n):
        sum[li[i] + li[j]] = (i, j)
print("IMPOSSIBLE")