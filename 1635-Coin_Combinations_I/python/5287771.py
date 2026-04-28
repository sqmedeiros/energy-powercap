a, b = map(int,input().split())
c = [*map(int,input().split())]
d = [0] * (b+1)
d[0] = 1

for x in range(b+1):
    for e in c:
        if x + e <= b:
            d[x+e] = (d[x] + d[x+e]) % (10**9 + 7)

print(d[b])