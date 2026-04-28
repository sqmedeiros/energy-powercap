import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))

a = [(val, idx + 1) for idx, val in enumerate(arr)]
a.sort()

l, r = 0, n - 1
while l < r:
    total = a[l][0] + a[r][0]
    if total == k:
        print(a[l][1], a[r][1])
        exit(0)
    elif total < k:
        l += 1
    else:
        r -= 1

print("IMPOSSIBLE")