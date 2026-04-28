INF = 1000000000
n, desire = map(int, input().split())
numbers = list(map(int, input().split()))
c = [INF] * (desire + 1)
c[0] = 0

for i in range(desire):
    for j in numbers:
        if i + j <= desire:
            c[i + j] = min(c[i + j], c[i] + 1)

if c[desire] == INF:
    print(-1)
else:
    print(c[desire])













