n, x = map(int, input().split())
cn = [int(i) for i in input().split()]

a = [0]*(x+1)
a[0] = 1

for i in range(x):
    for c in cn:
        if i+c <= x:
            a[i+c] += a[i]
            a[i+c] %= 10**9 + 7

print(a[x])