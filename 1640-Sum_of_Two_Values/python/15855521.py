import sys

n, x = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

indexed = [(arr[i], i) for i in range(n)]
indexed.sort()

l, r = 0, n - 1
while l < r:
    s = indexed[l][0] + indexed[r][0]
    if s == x:
        print(indexed[l][1] + 1, indexed[r][1] + 1)
        sys.exit(0)
    elif s < x:
        l += 1
    else:
        r -= 1

print("IMPOSSIBLE")