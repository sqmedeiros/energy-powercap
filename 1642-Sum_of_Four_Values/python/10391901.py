n, m= map(int, input().split())
array = list(map(int, input().split()))

sum_map = {}
found = False

for i in range(n - 1, -1, -1):
    for j in range(i -1, -1, -1):
        target = m - array[i] - array[j]
        if target in sum_map:
            found = True
            print(i + 1, j + 1, sum_map[target][0] + 1, sum_map[target][1] + 1)
            break

    if found:
        break

    for j in range(i + 1, n):
        sum_map[array[i] + array[j]] = (i, j)

if not found:
    print("IMPOSSIBLE")