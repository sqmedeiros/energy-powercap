import sys
input = sys.stdin.readline
out = []

N = 10 ** 9 + 7

n, x = [int(i) for i in input().split()]
A = [int(i) for i in input().split()]

dp = [0 for _ in range(max(A))]
dp.append(1)
for i in range(x):
    s = 0
    for c in A:
        s += dp[-c]
    dp.append(s % N)

out.append(dp[-1])

print("\n".join(map(str, out)))