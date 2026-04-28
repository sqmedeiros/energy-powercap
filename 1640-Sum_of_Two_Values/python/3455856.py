n, target = map(int, input().split())
nums = list(map(int, input().split()))

a = []

for i in range(n):
    a.append([nums[i], i + 1])

a.sort()

lIdx, rIdx = 0, n - 1

while lIdx < rIdx:
    twosum = a[lIdx][0] + a[rIdx][0]

    if twosum == target:
        print(a[lIdx][1], a[rIdx][1])
        exit()

    elif twosum > target:
        rIdx = rIdx - 1

    else:
        lIdx = lIdx + 1

print("IMPOSSIBLE")