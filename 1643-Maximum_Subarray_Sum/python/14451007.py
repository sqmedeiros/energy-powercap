import sys


it = list(map(int, sys.stdin.buffer.read().split()))

n = it[0]

maxi = -(10**9)
total = 0
for i in range(1, n + 1):
    total += it[i]
    maxi = max(maxi, total)

    total = max(total, 0)

sys.stdout.write(str(maxi))