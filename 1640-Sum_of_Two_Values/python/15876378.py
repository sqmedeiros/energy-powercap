import sys

it = iter(sys.stdin.buffer.read().split())
n = int(next(it))
x = int(next(it))

a = [(int(next(it)), i) for i in range(1, n + 1)]
a.sort()

l, r = 0, n - 1
while l < r:
    s = a[l][0] + a[r][0]
    if s == x:
        sys.stdout.write(f"{a[l][1]} {a[r][1]}")
        break
    if s < x:
        l += 1
    else:
        r -= 1
else:
    sys.stdout.write("IMPOSSIBLE")