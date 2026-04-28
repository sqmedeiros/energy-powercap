n, x = map(int, input().split())
a = list(map(int, input().split()))
indexed_a = [(a[i], i + 1) for i in range(n)]
indexed_a.sort()

def binary_search(arr, target, start):
    l, r = start, len(arr) - 1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid][0] == target:
            return arr[mid][1]
        elif arr[mid][0] < target:
            l = mid + 1
        else:
            r = mid - 1
    return None

for i in range(n):
    complement = x - indexed_a[i][0]
    idx = binary_search(indexed_a, complement, i + 1)
    if idx:
        print(indexed_a[i][1], idx)
        break
else:
    print("IMPOSSIBLE")